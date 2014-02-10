class BNode(object):
    left, right, data = None, None, None
    
    def __init__(self, data):
        # initializes the data members
        self.left = None
        self.right = None
        self.data = data

class BTree(object):
    
    def __init__(self, root):
        # initializes the root member
        self.root = root
    
    def insert(self, root, node):
        
        if self.__insert_compare__(root, node):
            if root.left is None:
                root.left = node
                return root.left
            else:
                return root.left.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                return root.right
            else:
                return root.right.insert(root.right, node)
            
            return root.right
    
    def __insert_compare__(self, root, node):
        return node.data < root.data
     
    def find(self, root, data):
        # looks for a value into the tree
        if root == None:
            return root
        else:
            # if it has found it...
            if data == root.data:
                return root
            else:
                if data < root.data:
                    # left side
                    return self.find(root.left, data)
                else:
                    # right side
                    return self.find(root.right, data)
        
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            # computes the two depths
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            # returns the appropriate depth
            return max(ldepth, rdepth) + 1
        
    def minValue(self, root):
        # goes down into the left
        # arm and returns the last value
        while(root.left != None):
            root = root.left
        return root.data
            
    def size(self, root = None):
        if root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    def printTree(self, root):
        # prints the tree path
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print root.data,
            self.printTree(root.right)

    def printRevTree(self, root):
        # prints the tree path in reverse
        # order
        if root == None:
            pass
        else:
            self.printRevTree(root.right)
            print root.data,
            self.printRevTree(root.left)
    #print BTree.size(root)