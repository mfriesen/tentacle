#!python

import json
import os.path
import cherrypy
from cherrypy import tools
from mako.lookup import TemplateLookup

from tentacle.cthulhu.operation import CthulhuData

print '------------- CThulhu is alive'

current_dir = os.path.dirname(os.path.abspath(__file__))

class Action:

    @cherrypy.expose
    def spawns(self):
        response = cherrypy.response
        response.headers['Content-Type'] = 'application/json'
        spawns = CthulhuData.spawns()
        return json.dumps(spawns)

class Screed:
    
    @cherrypy.expose
    def index(self):        
        screeds = list()
        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('screed.html')

        return mytemplate.render(screeds=screeds)

    @cherrypy.expose
    def new(self):        
        #screeds = list()
        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('screed-new.html')

        return mytemplate.render()
    
class Root:
    
    @cherrypy.expose
    def index(self):        
        spawns = CthulhuData.spawns()

        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('index.html')

        return mytemplate.render(spawns=spawns)