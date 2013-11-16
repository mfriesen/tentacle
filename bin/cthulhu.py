#!/usr/bin/env python

import os
import cherrypy

from cherrypy.process.plugins import Monitor
from tentacle.cthulhu.zeroconf import querySpawns
from tentacle.cthulhu import Root

cherrypy.config.update("cherrypy.conf")

cthulhu = Root()
cherrypy.tree.mount(cthulhu, "/", "cthulhu.conf")

Monitor(cherrypy.engine, querySpawns, frequency=5).subscribe()

if hasattr(cherrypy.engine, 'block'):
    # 3.1 syntax
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    # 3.0 syntax
    cherrypy.server.quickstart()
    cherrypy.engine.start()