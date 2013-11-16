from tentacle.settings import *
from tentacle.spawn.zeroconf import startZeroConf
from tentacle.spawn.multicast import startSpawnMulticast

def startSpawn(name = DEFAULT_BONJOUR_NAME, regtype = DEFAULT_BONJOUR_REGTYPE, port = DEFAULT_BONJOUR_PORT):
    startZeroConf(name, regtype, port)
    startSpawnMulticast()

class Spawn(object):
    
    fullname = ""
    hosttarget = ""
    port = ""
    ipaddress = ""
    
    def __init__(self, fullname, hosttarget, port, ipaddress):
        self.ipaddress = ipaddress
        self.fullname = fullname
        self.hosttarget = hosttarget
        self.port = port
    