import unittest
import time
from threading import Thread

from tentacle.cthulhu.operation import *
from tentacle.shared.screed import Screed
from tentacle.spawn import startSpawn

class TestOperation(unittest.TestCase):
        
    def setUp(self):
        pass
        #self.screed = Screed()
        #self.assertTrue(len(self.screed.spawn_id) == 36)
        #self.screed.spawn_id = 'a2ddb78a-eefb-4598-a7e1-a97c8f37a56d'
    
    def test_query_spawns_one_spawn_returned(self):
        # given
        spawn = startSpawn()
        #thread = Thread(target = startSpawn)
        #thread.start()
        time.sleep(.5)
        # when
        querySpawns()

        # then
        #result = CthulhuData.spawn_list()
        
        #self.assertEqual(1, len(result))
        #thread.shutdown = True
        #self.assertEqual('{\n"cmds": [\n{\n"cmd": "hello"\n}\n], \n"spawn_id": "a2ddb78a-eefb-4598-a7e1-a97c8f37a56d"\n}', json)
        spawn.join()
            
if __name__ == '__main__':
    unittest.main()