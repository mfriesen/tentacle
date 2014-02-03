import unittest

from tentacle.dht.binary_tree import BTree

class TestBinaryTree(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_insert_01(self):
        # given
        tree = BTree()
        
        # when
        root = tree.insert(0)
        l00 = tree.insert(0)
        l10 = tree.insert(1)
        
        # then
        self.assertEqual(root, tree.root)
        self.assertEquals(root.left, l00)
        self.assertEquals(root.right, l10)
        self.assertIsNone(l00.left)
        self.assertIsNone(l00.right)
        self.assertIsNone(l10.left)
        self.assertIsNone(l10.right)
    
    def test_size_01(self):
        # given
        tree = BTree()
        
        # when
        result = tree.size(tree.root)
        
        # then
        self.assertEquals(0, result)

    def test_size_02(self):
        # given
        tree = BTree()
        tree.insert(0)
        
        # when
        result = tree.size(tree.root)
        
        # then
        self.assertEquals(1, result)
                
if __name__ == '__main__':
    unittest.main()
    
#          0    
#     10         00
#  100  010  001   000
#