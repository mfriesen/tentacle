#!/usr/bin/env python

import os
import cherrypy

from cherrypy.process.plugins import Monitor
from tentacle.server.cthulhu import Cthulhu
from tentacle.server.zeroconf import *

print '------------- CThulhu is alive'

cherrypy.config.update("cherrypy.conf")

cthulhu = Cthulhu()
cherrypy.tree.mount(cthulhu, "/", "root.conf")

Monitor(cherrypy.engine, querySpawns, frequency=5).subscribe()

if hasattr(cherrypy.engine, 'block'):
    # 3.1 syntax
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    # 3.0 syntax
    cherrypy.server.quickstart()
    cherrypy.engine.start()