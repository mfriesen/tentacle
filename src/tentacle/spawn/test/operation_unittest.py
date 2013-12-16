import unittest

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
        self.assertEqual('cat\nwindow\ndefenestrate\n', result)
    
    def test_process_screed_01(self):
        # given
        fn = "for v in ['cat', 'window', 'defenestrate']:\n\tprint v\n"
        screed = Screed()
        screed.add_fn(0, "loop", fn)
        
        # when
        result = run_screed(screed.to_json())
        
        # then
        self.assertEqual('{\n"screed": [\n{\n"loop": "cat\\nwindow\\ndefenestrate\\n"\n}\n]\n}', result)
    
if __name__ == '__main__':
    unittest.main()