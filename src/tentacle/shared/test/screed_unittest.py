import unittest
from tentacle.shared import to_json
from tentacle.shared import Screed

class TestScreed(unittest.TestCase):
    
    screed = ""
    
    def setUp(self):
        self.screed = Screed()
        self.assertTrue(len(self.screed.spawn_id) == 36)
        self.screed.spawn_id = 'a2ddb78a-eefb-4598-a7e1-a97c8f37a56d'
    
    def test_screed_hello(self):
        # given        
        self.screed.add_cmd("hello")
        
        # when
        json = to_json(self.screed)

        # then
        self.assertEqual('{\n"cmds": [\n{\n"cmd": "hello"\n}\n], \n"spawn_id": "a2ddb78a-eefb-4598-a7e1-a97c8f37a56d"\n}', json)
    
    def test_screed_hello_response(self):
        # given        
        screed0 = self.screed.add_cmd("hello")
        screed0.status_success()
        result0 = screed0.add_result()
        result0.os = "linux"
        
        # when
        json = to_json(self.screed)
        
        # then
        expect = '{\n"cmds": [\n{\n"cmd": "hello", \n"result": {\n"os": "linux"\n}, \n"status": "success"\n}\n], \n"spawn_id": "a2ddb78a-eefb-4598-a7e1-a97c8f37a56d"\n}'
        self.assertEqual(expect, json)
        
if __name__ == '__main__':
    unittest.main()