#!/usr/bin/env python

import argparse
from tentacle.settings import *
from tentacle.spawn import startSpawn

parser = argparse.ArgumentParser()
parser.add_argument('--name', help='the name of the spawn', default=DEFAULT_BONJOUR_NAME)
parser.add_argument('--regtype', help='the regtype of the spawn', default=DEFAULT_BONJOUR_REGTYPE)
parser.add_argument('--port', help='the port to use', default=DEFAULT_BONJOUR_PORT)
args = parser.parse_args()

print '------------- Spawn is alive'
startSpawn(args.name, args.regtype, args.port)