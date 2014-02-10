import unittest
import hashlib

from tentacle.dht.routing_table import distance, most_sign_bits

class TestRoutingTable(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_distance_01(self):
        # given
        id0 = 102   # 1010
        id1 = 183   # 0010
        expect = 81 # 1000
        
        # when
        result = distance(id0, id1)
        
        # then
        self.assertEqual(expect, result)
            
    def test_distance_02(self):
        # given
        id0 = hashlib.sha1("salt").digest()
        id1 = hashlib.sha1("salt").digest()
        expect = 0
        
        # when
        result = distance(id0, id1)
        
        # then
        self.assertEqual(expect, result)

    def test_distance_03(self):
        # given
        id0 = "123"
        id1 = "1"
        result = None
        
        # when
        try:
            result = distance(id0, id1)
            
        # then
        except Exception, e:
            self.assertEqual("('distance cannot be calculated length ', 3, ' != ', 1)", str(e))
            
        self.assertIsNone(result)
            
    def test_most_sign_bits_01(self):        
        # given
        s = "a"  # 0110 0001
        
        # when
        result = most_sign_bits(s)
        
        # then
        self.assertEquals("01100001", result)
    
    def test_most_sign_bits_02(self):
        # given
        s = "5"  # 0011 0101
        
        # when
        result = most_sign_bits(s)
        
        # then
        self.assertEquals("00110101", result)    
    
    def test_most_sign_bits_03(self):
        # given
        s = "10" # 0011 0001 0011 0000
        
        # when
        result = most_sign_bits(s)
        
        # then
        self.assertEquals("0011000100110000", result)    
        
if __name__ == '__main__':
    unittest.main()