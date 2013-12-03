
import uuid

from tentacle.shared.screed import Screed

spawn_id = uuid.uuid4()
        
class SpawnScreed(Screed):
    
    def __init__(self):
        super(SpawnScreed, self).__init__()
        #super.__init__()
        self.screed['spawn_id'] = str(spawn_id)
        #self.screed = dict()