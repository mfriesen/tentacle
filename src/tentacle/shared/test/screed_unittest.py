import unittest
from tentacle.shared.screed import Screed

class TestScreed(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_screed_hello(self):
        # given
        screed = Screed()
        screed.add_cmd("hello")
        
        # when
        json = screed.to_json()

        # then
        self.assertEqual('{\n"screed": {\n"cmds": [\n{\n"cmd": "hello"\n}\n]\n}\n}', json)
    
    def test_screed_hello_response(self):
        # given
        screed = Screed()
        screed.add_cmd("hello")
        screed.add_result(index = 0, text = "this is resulting text")        
        
        # when
        json = screed.to_json()
        
        # then
        expect = '{\n"screed": {\n"cmds": [\n{\n"cmd": "hello", \n"result": {\n"text": "this is resulting text"\n}\n}\n]\n}\n}'
        self.assertEqual(expect, json)
        
    def test_screed_load(self):
        # given
        screed = Screed()
        index = screed.add_cmd("hello")
        self.assertEqual(0, index)
        screed.add_result(index, "this is resulting text")        
        json = screed.to_json()
        
        # when
        screed2 = Screed()
        screed2.load(json)
        
        # then
        self.assertEqual(1, len(screed2.cmds()))
        self.assertEqual("hello", screed2.cmd(0))
        self.assertEqual("this is resulting text", screed2.result(0)['text'])
    
    def test_screed_status_success(self):
        # given
        screed = Screed()
        screed.add_cmd("hello")
        screed.status_success()            
        
        # when
        json = screed.to_json()
        
        # then
        expect = '{\n"screed": {\n"cmds": [\n{\n"cmd": "hello"\n}\n]\n}, \n"status": "success"\n}'
        self.assertEqual(expect, json)
        
if __name__ == '__main__':
    unittest.main()