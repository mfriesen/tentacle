import unittest

from tentacle.dht.routing_table import sha1_id
from tentacle.dht.dht_bucket_routing_table import DHTBucketRoutingTable, DHTBucketNode

class TestDHTBucketRoutingTable(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_constructor_01(self):
        # given
        
        id_ = "10"      # 0011 0001 0011 0000        
 
        # when
        result = DHTBucketRoutingTable(id_)
        
        # then
        self.assertEqual(0, len(result._routingTree._root._bucket))
        
    # test empty routing table
    def test_add_node_01(self):
        # given
        id_ = "10"      # 0011 0001 0011 0000
        node_id = "50"  # 0011 0101 0011 0000        
        rt = DHTBucketRoutingTable(id_)
        
        self.assertEqual(0, len(rt._routingTree._root._bucket))
 
        # when
        rt.add_node(node_id)
        
        # then
        self.assertEqual(1, len(rt._routingTree._root._bucket))
            
    # test adding duplicate nodes
    def test_add_node_02(self):
        # given
        id_ = "10"      # 0011 0001 0011 0000
        node_id = "50"  # 0011 0101 0011 0000        
        rt = DHTBucketRoutingTable(id_)
        
        self.assertEqual(0, len(rt._routingTree._root._bucket))
 
        # when
        rt.add_node(node_id)
        rt.add_node(node_id)
        
        # then
        self.assertEqual(1, len(rt._routingTree._root._bucket))

    # test add node and split bucket
    def test_add_node_03(self):
        # given
        id_ = sha1_id("10")
        
        rt = DHTBucketRoutingTable(id_)
        node_start_id = 50  # 0011 0101 0011 0000
        
        for i in range(1, DHTBucketNode.MAX_BUCKET_SIZE):
            node_id = str(int(node_start_id) + i)
            rt.add_node(sha1_id(node_id))
        
        self.assertEqual(DHTBucketNode.MAX_BUCKET_SIZE - 1, len(rt._routingTree._root._bucket))
 
        # when
        rt.add_node(node_start_id)
        
        # then
        # level 0
        node0 = rt._routingTree._root
        self.assertIsNone(node0._bucket)
        self.assertIsNotNone(node0._left)
        self.assertIsNotNone(node0._right)
        
        # level 1
        node_left1 = node0._left
        node_right1 = node0._right
        self.assertEqual(2, len(node_left1._bucket))
        self.assertEqual(6, len(node_right1._bucket))

    # test if split is all on one side, don't split    
    def test_add_node_04(self):
        # given
        id_ = pow(2, 160)

        rt = DHTBucketRoutingTable(id_)
        node_start_id = 50

        # when
        for node_id in range(node_start_id, node_start_id + DHTBucketNode.MAX_BUCKET_SIZE + 1):
            rt.add_node(node_id)

        # then
        node0 = rt._routingTree._root
        self.assertEqual(DHTBucketNode.MAX_BUCKET_SIZE, len(node0._bucket))
        self.assertIsNone(node0._left)
        self.assertIsNone(node0._right)
 
    # test adding nodes to one side, only keep MAX_BUCKET_SIZE    
    def test_add_node_05(self):
        # given
        id_ = pow(2, 160)
        
        rt = DHTBucketRoutingTable(id_)
        node_start_id = 50
         
        # when
        for node_id in range(node_start_id, node_start_id + DHTBucketNode.MAX_BUCKET_SIZE + 1):
            rt.add_node(node_id)

        # then
        node0 = rt._routingTree._root
        self.assertEqual(DHTBucketNode.MAX_BUCKET_SIZE, len(node0._bucket))
        self.assertEqual({51: 51, 52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58}, node0._bucket)
        self.assertIsNone(node0._left)
        self.assertIsNone(node0._right)
               
    # test only the bucket that includes ID is split
    def test_add_node_06(self):
        # given
        id_ = pow(2, 160)
        node_start_id = 50
        
        rt = DHTBucketRoutingTable(id_)
        root = rt._routingTree._root
         
        # when
        # fill left side
        for node_id in range(node_start_id, node_start_id + DHTBucketNode.MAX_BUCKET_SIZE + 1):
            rt.add_node(node_id)

        # fill right side
        for node_id in range(id_ - DHTBucketNode.MAX_BUCKET_SIZE - 1, id_ - 1):
            rt.add_node(node_id)
            
        # add MAX to left side
        rt.add_node(root._left._max)
        
        # add MIN to right side //// fix test
        rt.add_node(root._right._min + 1)
        
        # then
        self.assertIsNone(root._bucket)
        self.assertIsNotNone(root._left)
        self.assertIsNotNone(root._right)
        
        self.assertEqual(DHTBucketNode.MAX_BUCKET_SIZE, len(root._left._bucket))
        self.assertIsNone(root._left._left)
        self.assertIsNone(root._left._right)
        self.assertEqual({52: 52, 53: 53, 54: 54, 55: 55, 56: 56, 57: 57, 58: 58, 730750818665451459101842416358141509827966271489L: 730750818665451459101842416358141509827966271489L}, root._left._bucket)

        self.assertEqual(DHTBucketNode.MAX_BUCKET_SIZE, len(root._right._bucket))
        self.assertEqual({1461501637330902918203684832716283019655932542967L: 1461501637330902918203684832716283019655932542967L, 1461501637330902918203684832716283019655932542968L: 1461501637330902918203684832716283019655932542968L, 1461501637330902918203684832716283019655932542969L: 1461501637330902918203684832716283019655932542969L, 1461501637330902918203684832716283019655932542970L: 1461501637330902918203684832716283019655932542970L, 1461501637330902918203684832716283019655932542971L: 1461501637330902918203684832716283019655932542971L, 1461501637330902918203684832716283019655932542972L: 1461501637330902918203684832716283019655932542972L, 1461501637330902918203684832716283019655932542973L: 1461501637330902918203684832716283019655932542973L, 1461501637330902918203684832716283019655932542974L: 1461501637330902918203684832716283019655932542974L}, root._right._bucket)
    
if __name__ == '__main__':
    unittest.main()