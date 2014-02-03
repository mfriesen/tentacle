class BNode(object):
    left, right, data = None, None, None
    
    def __init__(self, data):
        # initializes the data members
        self.left = None
        self.right = None
        self.data = data

class BTree(object):
    
    def __init__(self):
        # initializes the root member
        self.root = None
    
    def insert(self, data):
        node = BNode(data)
        
        self.__insert__(self.root, node)
        
        if self.root is None:
            self.root = node
        
        return node

    def __insert__(self, root, node):
        # inserts a new data
        if root == None:
            # it there isn't any data
            # adds it and returns
            return node
        else:
            # enters into the tree
            if node.data <= root.data:
                # if the data is less than the stored one
                # goes into the left-sub-tree
                root.left = self.__insert__(root.left, node)
            else:
                # processes the right-sub-tree
                root.right = self.__insert__(root.right, node)

            return root
        
    def lookup(self, root, target):
        # looks for a value into the tree
        if root == None:
            return 0
        else:
            # if it has found it...
            if target == root.data:
                return 1
            else:
                if target < root.data:
                    # left side
                    return self.lookup(root.left, target)
                else:
                    # right side
                    return self.lookup(root.right, target)
        
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