import unittest
import hashlib

from tentacle.dht.routing_table import distance, to_binary, sha1_id

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
        id0 = "10"
        id1 = "51"
        expect = 41
        
        # when
        result = distance(id0, id1)
        
        # then
        self.assertEqual(expect, result)
        
    def test_distance_04(self):
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
            
    def test_to_binary_01(self):        
        # given
        s = "a"  # 0110 0001
        
        # when
        result = to_binary(s)
        
        # then
        self.assertEquals("01100001", result)
    
    def test_to_binary_02(self):
        # given
        s = "5"  # 0011 0101
        
        # when
        result = to_binary(s)
        
        # then
        self.assertEquals("00110101", result)    
    
    def test_to_binary_03(self):
        # given
        s = "10" # 0011 0001 0011 0000
        
        # when
        result = to_binary(s)
        
        # then
        self.assertEquals("0011000100110000", result)    
    
    def test_to_binary_04(self):
        # given
        s = 40 # 0010 1000
        
        # when
        result = to_binary(s)
        
        # then
        self.assertEquals("00101000", result)    

    def test_sha1_id_01(self):
        # given
        s = "sample string"
        
        # when
        result = sha1_id(s)
        
        # then
        self.assertEquals(206627792091191212784374861007573277743147468436L, result
                          )
if __name__ == '__main__':
    unittest.main()