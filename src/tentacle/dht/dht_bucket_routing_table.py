from tentacle.dht.routing_table import DHTRoutingTable, to_binary, distance
from tentacle.dht.binary_tree import BTree, BNode

class DHTBucketNode(BNode):
    
    MAX_BUCKET_SIZE = 20
    
    def __init__(self, data, level):
        super(DHTBucketNode, self).__init__(data)
        self.bucket = dict()
        self.level = level
        
    def add_node(self, id_):
        self.bucket[id_] = id_
        
    def is_bucket_full(self):
        return len(self.bucket) == DHTBucketNode.MAX_BUCKET_SIZE        

class DHTBucketBTree(BTree):
    
    def __init__(self, root):
        super(DHTBucketBTree, self).__init__(root)

    def find(self, root, data):

        if root == None:
            return root
        else:
            if self.__compare__(root.data, data):
                #print 'left'
                return root.left
            else:
                #print 'right'
                return root.right

    def __compare__(self, data0, data1):
        return round(data1) < data0

class DHTBucketRoutingTable(DHTRoutingTable):
    
    routingTree = None
    
    def __init__(self, id_):

        self.routingTree = DHTBucketBTree(DHTBucketNode(data = 0.5, level = 0))
        
        self._id = id_
        #bits = to_binary(id_)
        #print bits

        #node = self.routingTree.root
        #for s in bits:
            #data = float(s) * 0.5 + 0.1
            #next_node = DHTBucketNode(data = data)
            #node = self.routingTree.insert(node, next_node)
    
    def __create_node__(self, data, level):
        data = float(data) * 0.5 + 0.1
        node = DHTBucketNode(data = data, level = level)
        return node
    
    def add_node(self, node_id):
        #print node_id , " ", to_binary(node_id)
        node = self.__find_bucket__(node_id)
        node.add_node(node_id)
        
        if node.is_bucket_full():
            self.__split_bucket__(node)
    
    def __find_bucket__(self, node_id):
                
        node = self.routingTree.root
        d = distance(self._id, node_id)
        
        for s in to_binary(d):
            if s == "0" and node.left is None:
                break
            elif s == "1" and node.right is None:
                break
            else:
                node = node.right if s == "1" else node.left
                    
        return node
        
    def __split_bucket__(self, node):
        print '---- spliting- ---' , node.level
        #node.bucket.sort()
        
        if node.is_bucket_full():
            
            zero_list = list()
            one_list = list()
            
            for s in node.bucket:
                d = distance(self._id, s)
                bits = to_binary(d)
                #print bits , " " , bits[node.level]
                if bits[node.level] == "1":
                    one_list.append(s)
                else:
                    zero_list.append(s)
                        
            level = node.level + 1
            zero_node = self.__create_node__(0, level)            
            one_node = self.__create_node__(1, level)
            
            zero_node.bucket = zero_list
            one_node.bucket = one_list
            
            node.bucket = None
            node.left = zero_node
            node.right = one_node
            #print "ONE " , len(one_list) , " zero ", len(zero_list)
                    
            self.__split_bucket__(zero_node)
            self.__split_bucket__(one_node)
    
    def find_closest_node(self, node_id):
        # If we have no known nodes, exception!
        if len(self._nodes) == 0:
            raise RuntimeError, "No nodes in routing table!"