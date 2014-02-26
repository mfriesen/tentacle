import unittest

from tentacle.spawn import SpawnConfig
from tentacle.spawn.operation import run_fn
from tentacle.spawn.operation import run_screed
from tentacle.shared.screed import Screed

class TestOperation(unittest.TestCase):
    
    def setUp(self):
        pass
       
    def test_run_fn(self):
        # given
        fn = "for v in ['cat', 'window', 'defenestrate']:\n\tprint v\n"
        
        # when
        result = run_fn(fn)
        
        # then
        self.assertEqual('cat\nwindow\ndefenestrate', result)
    
    def test_process_screed_01(self):
        # given
        fn = "for v in ['cat', 'window', 'defenestrate']:\n\tprint v\n"
        screed = Screed()
        screed.add_fn(0, "loop", fn)
        spawnConfig = SpawnConfig()
        spawnConfig._spawn_id = '9dcc9258-3998-4012-b3cf-0b7bd70e0a4d'
        
        # when
        result = run_screed(spawnConfig, screed.to_json())
        
        # then
        expect = '{\n"screed": {\n"steps": [\n{\n"loop": "cat\\nwindow\\ndefenestrate"\n}\n]\n}, \n"spawn": {\n"id": "9dcc9258-3998-4012-b3cf-0b7bd70e0a4d"\n}\n}'
        self.assertEqual(expect, result)
    
if __name__ == '__main__':
    unittest.main()