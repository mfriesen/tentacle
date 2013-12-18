import unittest
import time

from tentacle.cthulhu.operation import querySpawns
from tentacle.cthulhu.operation import CthulhuData
from tentacle.spawn import SpawnThread

class TestOperation(unittest.TestCase):
        
    def setUp(self):
        pass
    
    def test_query_spawns_one_spawn_returned(self):
        # given
        spawn = SpawnThread()
        spawn.start()
        
        time.sleep(.5)
        
        # when
        querySpawns()

        # then
        result = CthulhuData.spawn_list()
        self.assertEqual(1, len(result))
        
        CthulhuData.stop()
        spawn.join()
        
            
if __name__ == '__main__':
    unittest.main()