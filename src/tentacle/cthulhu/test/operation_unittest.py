import unittest
import time
 
from tentacle.shared.screed import Screed
from tentacle.cthulhu.operation import querySpawns
from tentacle.cthulhu.operation import CthulhuData
from tentacle.spawn import SpawnThread

class TestOperation(unittest.TestCase):
        
    @classmethod
    def setUpClass(self):
        CthulhuData.__init__()
        
    @classmethod
    def tearDownClass(self):
        CthulhuData.cleanup()
                
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
                
        spawn.join()
    
    def test_send_invalid_screed(self):
        # given
        spawn = SpawnThread()
        spawn.start()
        
        time.sleep(.5)

        screed = Screed()
        screed.add_fn(0, "hostname", "sadsadas")
        
        # when
        results = CthulhuData.send_screed(screed)
        
        # then
        self.assertEqual(1, len(results))
        
        result = results[0]
        self.assertEquals("name 'sadsadas' is not defined", result.step(0)['hostname'])
        

if __name__ == '__main__':
    unittest.main()