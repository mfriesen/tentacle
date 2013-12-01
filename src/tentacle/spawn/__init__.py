
from tentacle.settings import *
from tentacle.spawn.discovery import MulticastDiscovery
        
def startSpawn(name = DEFAULT_BONJOUR_NAME, regtype = DEFAULT_BONJOUR_REGTYPE, port = DEFAULT_BONJOUR_PORT):

    discovery = MulticastDiscovery()
    
    discovery.start()
    
    try:
        try:
            while True:
                discovery.listen_for_message()
        except KeyboardInterrupt:
            pass
    finally:
        discovery.stop()