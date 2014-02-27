import unittest
import base64

from tentacle.dht.routing_table import distance, to_binary, sha1_id, byte_to_int

class TestRoutingTable(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_distance_01(self):
        # given
        id0 = 102   # 1010
        id1 = 183   # 0010
        expect = 209 # 1000
        
        # when
        result = distance(id0, id1)
        
        # then
        self.assertEqual(expect, result)
            
    def test_distance_02(self):
        # given
        id0 = sha1_id("salt")
        id1 = sha1_id("salt")
        expect = 0
        
        # when
        result = distance(id0, id1)
        
        # then
        self.assertEqual(expect, result)

    def test_distance_03(self):
        # given
        id0 = "10"
        id1 = "51"
        expect = 57
        
        # when
        result = distance(id0, id1)
        
        # then
        self.assertEqual(expect, result)
            
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
        self.assertEquals(206627792091191212784374861007573277743147468436L, result)

    def test_byte_to_int_01(self):
        # given
        bytes_ = base64.b64decode("s6s1sj0aMsjo0fAFMAYObQwHAZU=")
        
        # when
        result = byte_to_int(bytes_)
        
        # then
        self.assertEqual(1025727453009050644114422909938179475956677673365, result)
        
if __name__ == '__main__':
    unittest.main()