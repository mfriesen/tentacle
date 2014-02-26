from StringIO import StringIO
import unittest
import urllib

from cherrypy.lib.httputil import Host
import cherrypy

from tentacle.cthulhu import Root, ActionRoot, ScreedRoot 
from tentacle.cthulhu.datastore import *

local = Host('127.0.0.1', 50000, "")
remote = Host('127.0.0.1', 50001, "")

def setUpModule():
    cherrypy.config.update({'environment': "test_suite"})

    # prevent the HTTP server from ever starting
    cherrypy.server.unsubscribe()

    root = Root()
    root.action = ActionRoot()
    root.screed = ScreedRoot()

    cherrypy.tree.mount(root, '/')
    cherrypy.engine.start()
    
setup_module = setUpModule

def tearDownModule():
    cherrypy.engine.exit()
teardown_module = tearDownModule

class BaseCherryPyTestCase(unittest.TestCase):
    
    def webapp_request(self, path='/', method='GET', qs="", **kwargs):
        headers = [('Host', '127.0.0.1')]
        fd = None

        if method in ['POST', 'PUT']:
            
            if qs == "":
                qs = urllib.urlencode(kwargs)
            
            headers.append(('content-type', 'application/x-www-form-urlencoded'))
            headers.append(('content-length', '%d' % len(qs)))
            fd = StringIO(qs)
            qs = None
        elif kwargs:
            qs = urllib.urlencode(kwargs)

        # Get our application and run the request against it
        app = cherrypy.tree.apps['']
        # Let's fake the local and remote addresses
        # Let's also use a non-secure scheme: 'http'
        request, response = app.get_serving(local, remote, 'http', 'HTTP/1.1')
        try:
            response = request.run(method, path, qs, 'HTTP/1.1', headers, fd)
        finally:
            if fd:
                fd.close()
                fd = None

        if response.output_status.startswith('500'):
            print response.body
            raise AssertionError("Unexpected error")

        # collapse the response into a bytestring
        response.collapse_body()
        return response
    
class TestCthulhu(BaseCherryPyTestCase):
        
    def setUp(self):
        pass
            
    def test_index(self):
        response = self.webapp_request('/')
        self.assertEqual(response.output_status, '200 OK')
    
    def test_edit_get_01(self):
        response = self.webapp_request('/screed/edit')
        self.assertEqual(response.output_status, '200 OK')
    
    # save screed with 1 steps
    def test_edit_post_01(self):
        
        response = self.webapp_request('/screed/edit', 'POST', qs="name=123&description=332&type=Python&steps=xvxcvxcvxcv")

        self.assertEqual(response.output_status, '200 OK')
        print response.body
        self.assertTrue(int(response.body[0]) > 0)
        base = get_screed(response.body[0])
        self.assertIsNotNone(base)
        expect = u'{\n"screed": {\n"steps": [\n{\n"fn": "xvxcvxcvxcv"\n}\n]\n}\n}'
        self.assertEqual(expect, base.text)

    # save screed with 2 steps
    def test_edit_post_02(self):
        
        response = self.webapp_request('/screed/edit', 'POST', qs="name=123&description=332&type=Python&steps=xvxcvxcvxcv&steps=qweqweqweqw")

        self.assertEqual(response.output_status, '200 OK')
        print response.body
        self.assertTrue(int(response.body[0]) > 0)
        base = get_screed(response.body[0])
        self.assertIsNotNone(base)
        expect = '{\n"screed": {\n"steps": [\n{\n"fn": "xvxcvxcvxcv"\n}, \n{\n"fn": "qweqweqweqw"\n}\n]\n}\n}'
        self.assertEqual(expect, base.text)

    # save screed with 0 steps
    def test_edit_post_03(self):
        
        response = self.webapp_request('/screed/edit', 'POST', qs="name=123&description=332&type=Python")

        self.assertEqual(response.output_status, '200 OK')
        print response.body
        self.assertTrue(int(response.body[0]) > 0)
        base = get_screed(response.body[0])
        self.assertIsNotNone(base)
        expect = '{\n"screed": {\n"steps": []\n}\n}'
        self.assertEqual(expect, base.text)
        
if __name__ == '__main__':
    unittest.main()