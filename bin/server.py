#!/usr/bin/env python

import os
import cherrypy
from tentacle.server.cthulhu import Cthulhu

print 'STARTING server ----------'
#print os.path.dirname(os.path.abspath(__file__)) + '/webroot' 
                   
#cherrypy.config.update({
#                       'tools.staticdir.debug': True,
#                        'log.screen': True,
#                            'tools.staticdir.root':os.path.dirname(os.path.abspath(__file__)) + '/webroot',
#                            'server.socket_port': 8080,
#                        }) 
#cherrypy.quickstart(Cthulhu())

#class Root(object):
#    @cherrypy.expose
#    def index(self):
#        pass

#config = {
#    '/webroot':{
#    'tools.staticdir.on': True,
#    'tools.staticdir.dir': os.path.join(os.path.dirname(__file__), 'webroot')
#    }
#}

#cherrypy.tree.mount(Root(), '/', config = config)
#cherrypy.engine.start()
#cherrypy.engine.block()
#print 'ALL DONE'

#import cherrypy
#from root.roothandler import Root

cherrypy.config.update("cherrypy.conf")

cherrypy.tree.mount(Cthulhu(), "/", "root.conf")

if hasattr(cherrypy.engine, 'block'):
    # 3.1 syntax
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    # 3.0 syntax
    cherrypy.server.quickstart()
    cherrypy.engine.start()