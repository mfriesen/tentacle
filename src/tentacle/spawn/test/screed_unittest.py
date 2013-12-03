import unittest
from tentacle.spawn.screed import SpawnScreed

class TestScreed(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_screed(self):
        # given
        screed = SpawnScreed()
        screed.add_cmd("hello")
        self.assertEqual(36, len(screed.screed['spawn_id']))
        screed.screed['spawn_id'] = "9baa1582-5031-4e37-b5ea-d7907c99880e"
        
        # when
        json = screed.to_json()

        # then
        self.assertEqual('{\n"screed": {\n"cmds": [\n{\n"cmd": "hello"\n}\n], \n"spawn_id": "9baa1582-5031-4e37-b5ea-d7907c99880e"\n}\n}', json)
        
if __name__ == '__main__':
    unittest.main()