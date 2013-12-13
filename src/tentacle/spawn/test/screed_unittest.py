import unittest
#import socket
#import sys
#from StringIO import StringIO
import sys
import StringIO
import contextlib
from cStringIO import StringIO

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
    
    
    def test_bleh(self):
        #socket.gethostname()
        #__import__("socket")
        #exec('import %s' % 'socket')
        #exec('import %s' % 'platform')
        
        #buffer = StringIO()
        #sys.stdout = buffer

        #exec 'print 5'
  
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        #exec("for v in ['cat', 'window', 'defenestrate']:\n\tprint v\n")
        exec("import socket\nprint socket.gethostname()")
        sys.stdout = old_stdout

        print redirected_output.getvalue()
        
        #exec "for v in ['cat', 'window', 'defenestrate']:\n\tprint v\n"
        #g = eval("import socket\nsocket.gethostname()")
        #g = f('''print "ECHO"''')(31)
        #print eval("__import__(\"socket\")\nsocket.gethostname()")
        #g = eval("socket.gethostname()")
        #x = exec "lambda : socket.gethostname()"
        
        #sys.stdout = sys.__stdout__

        #print g
        #print e 
        #g = lambda : socket.gethostname()
        
        #print g()
        
if __name__ == '__main__':
    unittest.main()