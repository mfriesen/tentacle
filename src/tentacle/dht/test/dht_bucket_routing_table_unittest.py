import unittest

from tentacle.dht.routing_table import distance, most_sign_bits
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
        node = result.routingTree.root
        
        # 0011 0001 0011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 011 0001 0011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 11 0001 0011 0000
        self.assertIsNone(node.left)
        self.assertIsNotNone(node.right)
        node = node.right

        # 1 0001 0011 0000
        self.assertIsNone(node.left)
        self.assertIsNotNone(node.right)
        node = node.right
        
        # 0001 0011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 001 0011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 01 0011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 1 0011 0000
        self.assertIsNone(node.left)
        self.assertIsNotNone(node.right)
        node = node.right
        
        # 0011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 011 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 11 0000
        self.assertIsNone(node.left)
        self.assertIsNotNone(node.right)
        node = node.right

        # 1 0000
        self.assertIsNone(node.left)
        self.assertIsNotNone(node.right)
        node = node.right
        
        # 0000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left

        # 000
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left

        # 00
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        node = node.left
        
        # 0
        self.assertIsNotNone(node.left)
        self.assertIsNone(node.right)
        
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