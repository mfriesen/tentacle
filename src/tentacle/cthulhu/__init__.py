#!python

import os.path
import cherrypy
from cherrypy import tools
from mako.lookup import TemplateLookup

from tentacle.cthulhu.operation import CthulhuData

print '------------- CThulhu is alive'

current_dir = os.path.dirname(os.path.abspath(__file__))

class Action:
    
    @cherrypy.expose
    def sendmsg(self):
        pass  
        
class Root:
    
    @cherrypy.expose
    def index(self):
        
        spawns = CthulhuData.spawn_list()
        print '# of spawns'
        print len(spawns)

        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('index.html')

        return mytemplate.render(name='world', spawns=spawns)