import unittest

from tentacle.dht.binary_tree import BTree, BNode

class TestBinaryTree(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_insert_01(self):
        # given
        tree = BTree(BNode(0.5))
        l00 = BNode(0)
        l10 = BNode(1)
        
        # when
        result_left = tree.insert(tree.root, l00)
        result_right = tree.insert(tree.root, l10)
        
        # then
        self.assertEquals(tree.root.left, l00)
        self.assertEquals(tree.root.right, l10)
        self.assertEquals(tree.root.left, result_left)
        self.assertEquals(tree.root.right, result_right)
        self.assertIsNone(l00.left)
        self.assertIsNone(l00.right)
        self.assertIsNone(l10.left)
        self.assertIsNone(l10.right)
   
    # test inserting multiple nodes on 1 side of the tree
    def test_insert_02(self):
        # given
        tree = BTree(BNode(0.5))
        l00 = BNode(0)
        l10 = BNode(0.5)
        l11 = BNode(1)
        
        # when
        result0 = tree.insert(tree.root, l00)
        result1 = tree.insert(result0, l10)
        result2 = tree.insert(result1, l11)
        
        # then
        self.assertEquals(tree.root.left, l00)
        self.assertEquals(tree.root.left, result0)
        self.assertIsNone(tree.root.right)

        self.assertEquals(result0.right, l10)
        self.assertEquals(result0.right, result1)
        self.assertIsNone(result0.left)

        self.assertEquals(result1.right, l11)
        self.assertEquals(result1.right, result2)
        self.assertIsNone(result1.left)
         
    def test_size_01(self):
        # given
        tree = BTree(BNode(9))
        
        # when
        result = tree.size(tree.root)
        
        # then
        self.assertEquals(1, result)

    def test_size_02(self):
        # given
        tree = BTree(BNode(0))
        tree.insert(tree.root, BNode(0))
        
        # when
        result = tree.size(tree.root)
        
        # then
        self.assertEquals(2, result)
                
    def test_find_01(self):
        # given
        tree = BTree(BNode(0.5))
        l00 = BNode(0)
        l10 = BNode(1)
        
        # when
        tree.insert(tree.root, l00)
        tree.insert(tree.root, l10)

        # when
        result0 = tree.find(tree.root, 0)
        result10 = tree.find(tree.root, 1)
        
        # then
        self.assertEqual(l00, result0)
        self.assertEqual(l10, result10)
        
if __name__ == '__main__':
    unittest.main()
    
#          0    
#     10         00
#  100  010  001   000
#