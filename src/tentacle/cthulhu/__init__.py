#!python

import os.path
import cherrypy
from cherrypy import tools
from mako.lookup import TemplateLookup

from tentacle.cthulhu.zeroconf import Zeroconf
from tentacle.cthulhu.multicast import sendMessage

print '------------- CThulhu is alive'

current_dir = os.path.dirname(os.path.abspath(__file__))

class Action:
    
    @cherrypy.expose
    def sendmsg(self):
        sendMessage('this is our awesome message')
        
class Root:
    
    action = Action()
    
    @cherrypy.expose
    def index(self):
        spawns = Zeroconf.spawn_list()
        print '# of spawns'
        print len(spawns)
        print current_dir

        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('index.html')

        return mytemplate.render(name='world', spawns=spawns)