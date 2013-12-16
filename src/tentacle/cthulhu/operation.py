from tentacle.shared.screed import Screed
from tentacle.cthulhu.discovery import MulticastDiscovery

def singleton(cls):
    return cls()

@singleton
class CthulhuData(MulticastDiscovery):
    
    _spawns = None
    _discovery = None

    def __init__(self):
        self._spawns = dict()
        self.start()

    def spawn_add(self, screed):
        spawn_id = screed.spawn_id
        self._spawns[spawn_id] = screed
        
    def spawn_list(self):
        return self._spawns.values()
        
def querySpawns():
    print 'querying for spawns....'
    
    screed = Screed()
    screed.add_fn(0, "hostname", "import socket\nprint socket.gethostname()")
    response = CthulhuData.send_message(screed)
    print '------------ response start --------------------------'
    print response
    #print response.status
    #print response.message
    print '------------ response end --------------------------'
    #Zeroconf.querySpawns()
    
def sendTestMessage():
    response = CthulhuData.send_message(Screed('this is our awesome message'))
    print '------------ response start --------------------------'
    print response.server
    print response.status
    print response.message
    print '------------ response end --------------------------'