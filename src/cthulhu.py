#!/usr/bin/env python

import cherrypy

from cherrypy.process.plugins import Monitor
from tentacle.cthulhu.operation import querySpawns
from tentacle.cthulhu import Root, ActionRoot, ScreedRoot

cherrypy.config.update({'server.thread_pool' : 10,
                        'server.socket_port' : 8080,
                        'tools.sessions.on' : True
                       })

config = {
'/' : { 'tools.staticdir.root' : '/Users/slycer/Documents/workspace/python/tentacle/src/tentacle/cthulhu/webroot' },
'/css' : { 'tools.staticdir.on': True, 'tools.staticdir.dir' : 'css' },
'/js' : { 'tools.staticdir.on': True, 'tools.staticdir.dir' : 'js' },
'/images' : { 'tools.staticdir.on': True, 'tools.staticdir.dir' : 'images' },
}

root = Root()
root.action = ActionRoot()
root.screed = ScreedRoot()
cherrypy.tree.mount(root, "/", config=config)

Monitor(cherrypy.engine, querySpawns, frequency=5).subscribe()

cherrypy.engine.start()
cherrypy.engine.block()