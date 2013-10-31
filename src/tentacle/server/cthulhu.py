import cherrypy

from mako.template import Template

class Cthulhu(object):
    
    spawns = 0
    
    @cherrypy.expose
    def index(self):
        mytemplate = Template(filename='webroot/index.html')
        return mytemplate.render()
    
    def addSpawn(self):
        print 'adding spawn'
        print self.spawns
        self.spawns = self.spawns + 1
        
    