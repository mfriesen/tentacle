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