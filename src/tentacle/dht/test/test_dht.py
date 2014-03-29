import unittest
import mock
import base64
import socket

from tentacle.dht.routing_table import sha1_id

from tentacle.dht import DHT, DHTResponse
    
class TestDht(unittest.TestCase):
    
    def setUp(self):
        pass

    # test add host/port to RoutingTable
    def test_add_node_01(self):
        # given
        dht = DHT(id_=sha1_id("salt"))
        data = base64.b64decode("ZDI6aXA2OjJH1ovP/TE6cmQyOmlkMjA6HbzsI8Zpc1H/Suwpzbqr8vvjRmdlMTp0MjphYTE6eTE6cmU=")
        dht.__create_socket__ = mock.Mock(return_value = None)
        dht.__send_request__ = mock.Mock(return_value = DHTResponse(data))
        
        # when
        dht.add_node("67.215.242.138", 6881)
        
        # result        
        root = dht._routing_table._root
        self.assertEquals(1, len(root._bucket._nodes))
        self.assertIsNone(root._left)
        self.assertIsNone(root._right)
         
    # test okay ping response
    def test_ping_01(self):
        # given
        dht = DHT(id_=sha1_id("salt"))
        data = base64.b64decode("ZDI6aXA2OjJH1ovP/TE6cmQyOmlkMjA6HbzsI8Zpc1H/Suwpzbqr8vvjRmdlMTp0MjphYTE6eTE6cmU=")
        dht.__create_socket__ = mock.Mock(return_value = None)
        dht.__send_request__ = mock.Mock(return_value = DHTResponse(data))
        
        # when
        result = dht.ping("67.215.242.138", 6881)
        
        # result
        self.assertEqual("aa", result.transaction_id())
        self.assertTrue(result.is_response())
        self.assertFalse(result.is_query())
        self.assertFalse(result.is_error())
        
        dic = result.data()
        self.assertEquals("1DBCEC23C6697351FF4AEC29CDBAABF2FBE34667", base64.b16encode(dic['id']))

    # test find self
    def test_find_closest_nodes_01(self):
        # given
        dht = DHT(id_=sha1_id("salt"))
        data = base64.b64decode("ZDI6aXA2OjJH1ovP/TE6cmQyOmlkMjA6HbzsI8Zpc1H/Suwpzbqr8vvjRmdlMTp0MjphYTE6eTE6cmU=")
        dht.__create_socket__ = mock.Mock(return_value = None)
        dht.__send_request__ = mock.Mock(return_value = DHTResponse(data))
        
        # when
        dht.add_nodes_default()
        result = dht.find_closest_nodes(dht._id)
        
        # then
        self.assertEquals(1, len(result))
        self.assertEquals(dht._id, result[0]._id)
        self.assertEquals(socket.gethostbyname(socket.gethostname()), result[0]._host)
        self.assertEquals(1111, result[0]._port)
        
        root = dht._routing_table._root
        self.assertEquals(2, len(root._bucket._nodes))
        self.assertIsNone(root._left)
        self.assertIsNone(root._right)

    # response find NON self Node_ID
    def test_find_closest_nodes_02(self):
        # given 
        find_node_id = sha1_id("test node")
        dht = DHT(id_=sha1_id("salt"))
        
        # ping request
        data1 = base64.b64decode("ZDI6aXA2OjJH1ovP/TE6cmQyOmlkMjA6HbzsI8Zpc1H/Suwpzbqr8vvjRmdlMTp0MjphYTE6eTE6cmU=")
        dht.__create_socket__ = mock.Mock(return_value = None)
        dht.__send_request__ = mock.Mock(return_value = DHTResponse(data1))

        data2 = base64.b64decode("ZDI6aXA2OjJH1ov8ODE6cmQyOmlkMjA6HbzsI8Zpc1H/Suwpzbqr8vvjRmc1Om5vZGVzNDE2OrOrNbI9GjLI6NHwBTAGDm0MBwGVJUygHJKOn0rEaSOaULMo/u1Afw+X1Kx9Qwq2O7DHLO9b+W0Ap234h2XQmB/m83EiQTK6AbJ8zTFCD3NE622nFPnpiP39xDSfNBbzUR7UBQ3a1ts0gFvoFSKFlQFX2Kd+sj38y8MgoaxPo21McW3cDw/7SZw0R5ypPiy9BNpTbGQzTAK+3k/i+oYBFdHZhQ3e+lYygjlNJc7KtsXKXO1dRUN3NU7JFgICDVphT/GcFQn6i/gtoBoFgeUQVV1yCdEEnO4z5qHs4VFlOBcQy5UqlkOmMh/PqiYcR9iQNuH2ZE4NnBqgoooC6U68st6iF0di2HI5A9M7sKu5l03VuMRzNI3JCZIf2KLwT59VcAviVtAkIkb4kLKbhDnap1TYAx+1OMLqH4S1c80wM7Im3z+h2eT67Bk+mLkMUOm11i/GLHEmg+2eZ2k8oTW8nvfQeuHRuSdPFkNMlnacB1QjGFm4YENjhN1+EU8ixe1l8lxjV3tmCMTeO5l6mJ2bR/b14v3cwoImjU1KsAw7MvBxZTE6dDI6YWExOnkxOnJl")
        dht.__create_socket__ = mock.Mock(return_value = None)
        dht.__send_request__ = mock.Mock(return_value = DHTResponse(data2))

        # when
        dht.add_nodes_default()
        result = dht.find_closest_nodes(find_node_id)
        
        # then
        self.assertEquals(7, len(result))
        
        root = dht._routing_table._root
        self.assertEquals(7, len(root._left._bucket._nodes))
        self.assertIsNone(root._left._left)
        self.assertIsNone(root._left._right)
        
        self.assertEquals(7, len(root._right._left._bucket._nodes))
        self.assertEquals(3, len(root._right._right._bucket._nodes))
        
if __name__ == '__main__':
    unittest.main()