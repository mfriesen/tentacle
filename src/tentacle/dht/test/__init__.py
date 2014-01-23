import unittest
import hashlib

from tentacle.dht import DHT

class TestDht(unittest.TestCase):
    
    def setUp(self):
        self.dht = DHT(id_=hashlib.sha1("this salts the ID TODO change this").digest())
    
    # test okay ping response
    def test_ping_01(self):
        # given
        
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
    
    """
    message dictionaries with a "y" value of "e", 
    contain one additional key "e". 
    The value of "e" is a list. 
    The first element is an integer representing the error code. 
    The second element is a string containing the error message.
    """
    
if __name__ == '__main__':
    unittest.main()