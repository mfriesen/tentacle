import cherrypy

from tentacle.server.zeroconf import Zeroconf
from mako.template import Template
from mako.lookup import TemplateLookup

class Cthulhu(object):
    
    @cherrypy.expose
    def index(self):
        spawns = Zeroconf.spawn_list()
#        for w in spawns:
#            print '----hi ----'
#            print w.fullname
        print '# of spawns'
        print len(spawns)
#        mytemplate = Template(filename='webroot/index.html')
#        mytemplate = Template(filename='webroot/index.txt')
        #mytemplate = Template("hello, ${arjunaName}!")
#        return mytemplate.render(arjunaName="bleh")

        mylookup = TemplateLookup(directories=['webroot'])
        mytemplate = mylookup.get_template('index.html')
        #temp = mylookup.get_template('name.html').render()
        return mytemplate.render(name='world', spawns=spawns)