#!python
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
from cherrypy import tools

from tentacle.cthulhu.zeroconf import Zeroconf
from mako.lookup import TemplateLookup

class Root:
    @cherrypy.expose
    def index(self):
        spawns = Zeroconf.spawn_list()
        print '# of spawns'
        print len(spawns)
        print current_dir

        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('index.html')

        return mytemplate.render(name='world', spawns=spawns)