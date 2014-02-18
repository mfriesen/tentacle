class BNode(object):
    _left, _right, _data = None, None, None
    
    def __init__(self, data):
        # initializes the data members
        self._left = None
        self._right = None
        self._data = data

class BTree(object):
    
    def __init__(self, root):
        # initializes the root member
        self._root = root
    
    def insert(self, root, node):
        
        if self.__compare__(root._data, node._data):
            if root._left is None:
                root._left = node
                return root._left
            else:
                return root._left.insert(root._left, node)
        else:
            if root._right is None:
                root._right = node
                return root._right
            else:
                return root._right.insert(root._right, node)
            
            return root._right
    
    def __compare__(self, data0, data1):
        return data1 < data0
     
    def find(self, root, data):
        # looks for a value into the tree
        if root == None:
            return root
        else:
            # if it has found it...
            if data == root._data:
                return root
            else:
                if self.__compare__(root._data, data):
                    # left side
                    return self.find(root._left, data)
                else:
                    # right side
                    return self.find(root._right, data)
        
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            # computes the two depths
            ldepth = self.maxDepth(root._left)
            rdepth = self.maxDepth(root._right)
            # returns the appropriate depth
            return max(ldepth, rdepth) + 1
        
    def minValue(self, root):
        # goes down into the left
        # arm and returns the last value
        while(root._left != None):
            root = root._left
        return root._data
            
    def size(self, root = None):
        if root == None:
            return 0
        else:
            return self.size(root._left) + 1 + self.size(root._right)

    def printTree(self, root):
        # prints the tree path
        if root == None:
            pass
        else:
            self.printTree(root._left)
            print root._data,
            self.printTree(root._right)

    def printRevTree(self, root):
        # prints the tree path in reverse
        # order
        if root == None:
            pass
        else:
            self.printRevTree(root._right)
            print root._data,
            self.printRevTree(root._left)
    #print BTree.size(root)