#!python

import json
import os.path
import cherrypy
from cherrypy import tools
from mako.lookup import TemplateLookup

from tentacle.cthulhu.operation import CthulhuData
from tentacle.cthulhu.datastore import *
from tentacle.shared.screed import Screed
from aetypes import end

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
        screeds = get_screeds()
        
        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('screed.html')

        return mytemplate.render(screeds=screeds)

    @cherrypy.expose
    def edit(self, **kwargs):
                
        if cherrypy.request.method != 'GET':
            base = ScreedBase()
            screed = Screed()
            
            for key, value in kwargs.iteritems(): 
                setattr(base, key, value)            
            
            if 'steps' in kwargs:
                if hasattr(kwargs['steps'], "strip"):
                    screed.add_fn(0, "fn", kwargs['steps'])
                else:
                    idx = 0
                    for val in kwargs['steps']:                    
                        screed.add_fn(idx, "fn", val)
                        idx += 1
            
            base.text = screed.to_json()
            base = save_screed(base)

            return str(base.id)
        
        screed = None
        if 'id' in kwargs:
            screed = get_screed(kwargs['id'])
        
        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('screed-edit.html')

        return mytemplate.render(screed = screed)
    
class Root:
    
    @cherrypy.expose
    def index(self):        
        spawns = CthulhuData.spawns()

        mylookup = TemplateLookup(directories=[current_dir + '/webroot'])
        mytemplate = mylookup.get_template('index.html')

        return mytemplate.render(spawns=spawns)