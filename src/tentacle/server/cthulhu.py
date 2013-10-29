import cherrypy

from mako.template import Template

class Cthulhu(object):
    @cherrypy.expose
    def index(self):
        mytemplate = Template(filename='webroot/index.html')
        return mytemplate.render()