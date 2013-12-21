from tentacle.shared.screed import Screed
from tentacle.cthulhu.discovery import MulticastDiscovery

def singleton(cls):
    return cls()

@singleton
class CthulhuData(object):
    
    _spawns = None
    _discovery = None

    def __init__(self):
        self._spawns = list()
        self._discovery = [MulticastDiscovery()]
        
        for discovery in self._discovery:
            discovery.start()
        
    def send_screed(self, screed):
        
        results = list()
        for discovery in self._discovery:            
            messages = discovery.send_message(screed)
            for message in messages:
                screed_result = Screed()
                screed_result.load(message)
                results.append(screed_result)
            
        return results;
            
    def spawns(self):
        return self._spawns
    
    def cleanup(self):
        for discovery in self._discovery:
            discovery.stop()

def querySpawns():
    print 'querying for spawns....'
    
    screed = Screed()
    screed.add_fn(0, "hostname", "import socket\nprint socket.gethostname()")
    CthulhuData._spawns = CthulhuData.send_screed(screed)