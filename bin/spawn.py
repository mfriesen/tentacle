#!/usr/bin/env python

from tentacle.settings import *
from tentacle.spawn.zeroconf import start

print '------------- Spawn is alive'
start(DEFAULT_BONJOUR_NAME, DEFAULT_BONJOUR_REGTYPE, DEFAULT_BONJOUR_PORT)