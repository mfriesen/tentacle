import unittest

#from tentacle.dht.routing_table import distance, most_sign_bits
from tentacle.dht.dht_bucket_routing_table import DHTBucketRoutingTable

class TestDHTBucketRoutingTable(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_constructor_01(self):
        # given
        
        id_ = "10"      # 0011 0001 0011 0000        
 
        # when
        result = DHTBucketRoutingTable(id_)
        
        # then
        self.assertEqual(0, len(result.routingTree.root.bucket))
        
    # test empty routing table
    def test_add_node_01(self):
        # given
        id_ = "10"      # 0011 0001 0011 0000
        node_id = "50"  # 0011 0101 0011 0000        
        rt = DHTBucketRoutingTable(id_)
        
        self.assertEqual(0, len(rt.routingTree.root.bucket))
 
        # when
        rt.add_node(node_id)
        
        # then
        self.assertEqual(1, len(rt.routingTree.root.bucket))
            
    # test add node and split bucket
    def test_add_node_02(self):
        # given
        id_ = "10"            # 0011 0001 0011 0000
        node_start_id = "50"  # 0011 0101 0011 0000        
        rt = DHTBucketRoutingTable(id_)
        
        for i in range(1, 20):
            node_id = str(int(node_start_id) + i)
            rt.add_node(node_id)
        
        self.assertEqual(19, len(rt.routingTree.root.bucket))
 
        # when
        rt.add_node(node_start_id)
        
        # then
        self.assertEqual(20, len(rt.routingTree.root.bucket))

if __name__ == '__main__':
    unittest.main()