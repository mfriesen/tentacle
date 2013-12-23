import unittest
from tentacle.shared.screed import Screed

class TestScreed(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_screed_load(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nprint socket.gethostname()")
        json = screed.to_json()
        
        # when
        screed2 = Screed()
        screed2.load(json)
        
        # then
        self.assertEqual(1, len(screed2.get("screed")))
        
        expect = '{\n"screed": [\n{\n"hostname": "import socket\\nprint socket.gethostname()"\n}\n]\n}'
        self.assertEqual(expect, screed2.to_json())
    
    def test_screed_status_success(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nprint socket.gethostname()")
        screed.status_success(0)
        screed.status_success()            
        
        # when
        json = screed.to_json()
        
        # then
        expect = '{\n"screed": [\n{\n"hostname": "import socket\\nprint socket.gethostname()", \n"status": "success"\n}\n], \n"status": "success"\n}'
        self.assertEqual(expect, json)
    
    def test_screed_add_fn_step0(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nsocket.gethostname()")
        
        # when
        json = screed.to_json()
        
        # then
        expect = '{\n"screed": [\n{\n"hostname": "import socket\\nsocket.gethostname()"\n}\n]\n}'
        self.assertEqual(expect, json)  
    
    def test_screed_add_fn_step0_2(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nprint socket.gethostname()")
        screed.add_fn(0, "os", "import os\nprint os.name")
        
        # when
        json = screed.to_json()
        
        # then
        expect = '{\n"screed": [\n{\n"hostname": "import socket\\nprint socket.gethostname()", \n"os": "import os\\nprint os.name"\n}\n]\n}'
        self.assertEqual(expect, json)  
    
    def test_screed_add_fn_steps(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nsocket.gethostname()")
        screed.add_fn(5, "os", "import os\nprint os.name")
        
        # when
        json = screed.to_json()
        
        # then
        expect = '{\n"screed": [\n{\n"hostname": "import socket\\nsocket.gethostname()"\n}, \n{}, \n{}, \n{}, \n{}, \n{\n"os": "import os\\nprint os.name"\n}\n]\n}'
        self.assertEqual(expect, json)  
        
    def test_screed_steps(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nprint socket.gethostname()")
        json = screed.to_json()
        
        # when
        screed2 = Screed()
        screed2.load(json)
        
        # then
        steps = screed2.steps()
        self.assertEqual(1, len(steps))
        
        for s in steps:
            for key in s:
                expect = u'import socket\nprint socket.gethostname()'
                self.assertEqual('hostname', key)
                self.assertEqual(expect, s[key])
        
    def test_screed_step_0(self):
        # given
        screed = Screed()
        screed.add_fn(0, "hostname", "import socket\nsocket.gethostname()")
        
        # when
        result = screed.step(0)
        
        # then
        self.assertEqual("import socket\nsocket.gethostname()", result["hostname"])
        
    def test_add_0(self):
        # given
        screed = Screed()
        screed.add("spawn", {'id': 4098})
        screed.add("spawn", {'sape': 4139})

        # when
        result = screed.to_json()
                 
        # then
        self.assertEqual('{\n"screed": [], \n"spawn": {\n"id": 4098, \n"sape": 4139\n}\n}', result)
        
if __name__ == '__main__':
    unittest.main()