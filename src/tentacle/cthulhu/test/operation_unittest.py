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
        results = CthulhuData.spawns()
        self.assertEqual(1, len(results))
        
        screed = results[0]
        self.assertEqual(1, len(screed.steps()))
        
        step_dic = screed.step(0)
        self.assertTrue(len(step_dic['hostname']) > 0)
                
        CthulhuData.cleanup()
        spawn.join()
            
if __name__ == '__main__':
    unittest.main()