import unittest
import hashlib
import struct
import mock
import base64

from tentacle.dht.bencode import bencode, bdecode

from tentacle.dht import DHT, DHTRequest, DHTResponse
    
class TestDht(unittest.TestCase):
    
    def setUp(self):
        self.dht = DHT(id_=hashlib.sha1("this salts the ID TODO change this").digest())
    
    # test okay ping response
    def test_ping_01(self):
        # given
        self.dht.__create_socket__ = mock.Mock(return_value = None)
        self.dht.__send_request__ = mock.Mock(return_value = DHTResponse("d1:rd2:id20:mnopqrstuvwxyz123456e1:t2:aa1:y1:re"))
        
        # when
        result = self.dht.ping()
        
        # result
        self.assertEqual("aa", result.transaction_id())
        self.assertTrue(result.is_response())
        self.assertFalse(result.is_query())
        self.assertFalse(result.is_error())
        
        dic = result.response_dic()
        self.assertEquals("mnopqrstuvwxyz123456", dic['id'])
    
    def test_find_node_01(self):
        # given
        node_id = "AJDLJASDLKJSALDJASLDK"
        
        self.dht.__create_socket__ = mock.Mock(return_value = None)
        self.dht.__send_request__ = mock.Mock(return_value = DHTResponse("d1:rd2:id20:0123456789abcdefghij5:nodes9:def456...e1:t2:aa1:y1:re"))

        # when
        result = self.dht.find_node(node_id)
        
        # result
        self.assertEqual("aa", result.transaction_id())
        self.assertTrue(result.is_response())
        self.assertFalse(result.is_query())
        self.assertFalse(result.is_error())
        
        dic = result.response_dic()
        self.assertEquals("0123456789abcdefghij", dic['id'])
        self.assertEquals("def456...", dic['nodes'])

    def test_find_node_02(self):
        # given 
        data = base64.b64decode("ZDI6aXA2OjJH1ov8ODE6cmQyOmlkMjA6HbzsI8Zpc1H/Suwpzbqr8vvjRmc1Om5vZGVzNDE2OrOrNbI9GjLI6NHwBTAGDm0MBwGVJUygHJKOn0rEaSOaULMo/u1Afw+X1Kx9Qwq2O7DHLO9b+W0Ap234h2XQmB/m83EiQTK6AbJ8zTFCD3NE622nFPnpiP39xDSfNBbzUR7UBQ3a1ts0gFvoFSKFlQFX2Kd+sj38y8MgoaxPo21McW3cDw/7SZw0R5ypPiy9BNpTbGQzTAK+3k/i+oYBFdHZhQ3e+lYygjlNJc7KtsXKXO1dRUN3NU7JFgICDVphT/GcFQn6i/gtoBoFgeUQVV1yCdEEnO4z5qHs4VFlOBcQy5UqlkOmMh/PqiYcR9iQNuH2ZE4NnBqgoooC6U68st6iF0di2HI5A9M7sKu5l03VuMRzNI3JCZIf2KLwT59VcAviVtAkIkb4kLKbhDnap1TYAx+1OMLqH4S1c80wM7Im3z+h2eT67Bk+mLkMUOm11i/GLHEmg+2eZ2k8oTW8nvfQeuHRuSdPFkNMlnacB1QjGFm4YENjhN1+EU8ixe1l8lxjV3tmCMTeO5l6mJ2bR/b14v3cwoImjU1KsAw7MvBxZTE6dDI6YWExOnkxOnJl")

        self.dht.__create_socket__ = mock.Mock(return_value = None)
        self.dht.__send_request__ = mock.Mock(return_value = DHTResponse(data))

        # when
        result = self.dht.find_node(self.dht._id)
        
        # then
        self.assertEqual("aa", result.transaction_id())
        self.assertTrue(result.is_response())
        self.assertFalse(result.is_query())
        self.assertFalse(result.is_error())
        
        dic = result.response_dic()

    
if __name__ == '__main__':
    unittest.main()