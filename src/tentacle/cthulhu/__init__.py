#!python

import json
import os.path
import cherrypy
from cherrypy import tools
from mako.lookup import TemplateLookup

from tentacle.cthulhu.operation import CthulhuData
from tentacle.cthulhu.datastore import Datastore
from tentacle.shared.screed import Screed

print '------------- CThulhu is alive'

current_dir = os.path.dirname(os.path.abspath(__file__))

class ActionRoot:

    @cherrypy.expose
    def spawns(self):
        response = cherrypy.response
        response.headers['Content-Type'] = 'application/json'
        spawns = CthulhuData.spawns()
        return json.dumps(spawns)

class ScreedRoot:
    
    @cherrypy.expose
    def index(self):        
        screeds = list()
        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('screed.html')

        return mytemplate.render(screeds=screeds)

    @cherrypy.expose
    def new(self, screedid=""):        
        #screeds = list()
        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('screed-new.html')

        return mytemplate.render()
    
    @cherrypy.expose
    def save(self, screedName="", screedDescription="", screedType=""):
        
        screed = Screed()
        screed.name(screedName)
        screed.description(screedDescription)
        screed.typeValue(screedType)

        base = Datastore.save_screed(screed)
                
        return base
    
class Root:
    
    @cherrypy.expose
    def index(self):        
        spawns = CthulhuData.spawns()

        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('index.html')

        return mytemplate.render(spawns=spawns)