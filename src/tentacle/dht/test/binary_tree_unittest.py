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
        result_left = tree.insert(tree._root, l00)
        result_right = tree.insert(tree._root, l10)
        
        # then
        self.assertEquals(tree._root._left, l00)
        self.assertEquals(tree._root._right, l10)
        self.assertEquals(tree._root._left, result_left)
        self.assertEquals(tree._root._right, result_right)
        self.assertIsNone(l00._left)
        self.assertIsNone(l00._right)
        self.assertIsNone(l10._left)
        self.assertIsNone(l10._right)
   
    # test inserting multiple nodes on 1 side of the tree
    def test_insert_02(self):
        # given
        tree = BTree(BNode(0.5))
        l00 = BNode(0)
        l10 = BNode(0.5)
        l11 = BNode(1)
        
        # when
        result0 = tree.insert(tree._root, l00)
        result1 = tree.insert(result0, l10)
        result2 = tree.insert(result1, l11)
        
        # then
        self.assertEquals(tree._root._left, l00)
        self.assertEquals(tree._root._left, result0)
        self.assertIsNone(tree._root._right)

        self.assertEquals(result0._right, l10)
        self.assertEquals(result0._right, result1)
        self.assertIsNone(result0._left)

        self.assertEquals(result1._right, l11)
        self.assertEquals(result1._right, result2)
        self.assertIsNone(result1._left)
         
    def test_size_01(self):
        # given
        tree = BTree(BNode(9))
        
        # when
        result = tree.size(tree._root)
        
        # then
        self.assertEquals(1, result)

    def test_size_02(self):
        # given
        tree = BTree(BNode(0))
        tree.insert(tree._root, BNode(0))
        
        # when
        result = tree.size(tree._root)
        
        # then
        self.assertEquals(2, result)
                
    def test_find_01(self):
        # given
        tree = BTree(BNode(0.5))
        l00 = BNode(0)
        l10 = BNode(1)
        
        # when
        tree.insert(tree._root, l00)
        tree.insert(tree._root, l10)

        # when
        result0 = tree.find(tree._root, 0)
        result10 = tree.find(tree._root, 1)
        
        # then
        self.assertEqual(l00, result0)
        self.assertEqual(l10, result10)
        
if __name__ == '__main__':
    unittest.main()