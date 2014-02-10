from tentacle.dht.routing_table import DHTRoutingTable, most_sign_bits, distance
from tentacle.dht.binary_tree import BTree, BNode

class DHTBucketNode(BNode):
    
    MAX_BUCKET_SIZE = 20
    
    def __init__(self, data):
        super(DHTBucketNode, self).__init__(data)
        self.bucket = list()
        
    def add_node(self, id_):
        self.bucket.append(id_)
        
    def is_bucket_full(self):
        return len(self.bucket) == DHTBucketNode.MAX_BUCKET_SIZE        

class DHTBucketBTree(BTree):
    
    def __init__(self, root):
        super(DHTBucketBTree, self).__init__(root)

    def __insert_compare__(self, root, node):
        return round(node.data) < root.data

class DHTBucketRoutingTable(DHTRoutingTable):
    
    routingTree = None
    
    def __init__(self, id_):

        self.routingTree = DHTBucketBTree(DHTBucketNode(data = 0.5))
        
        self._id = id_
        bits = most_sign_bits(id_)

        node = self.routingTree.root
        for s in bits:
            data = float(s) * 0.5 + 0.1
            next_node = DHTBucketNode(data = data)
            node = self.routingTree.insert(node, next_node)
    
    def add_node(self, node_id):
        
        bits = most_sign_bits(node_id)
        start_node = self.routingTree.root
        
        node = self.__find_bucket__(start_node, bits)
        node.add_node(node_id)
        
        if node.is_bucket_full():
            self.__split_bucket__(node)
    
    def __find_bucket__(self, node, bits):
        
        if node.right is not None and node.left is not None:
            print 'bucket is FULL'
        else:
            print 'bucket not full'
            return node
        
    def __split_bucket__(self, node):
        print '---- spliting- ---'
        node.bucket.sort()
        
        for s in node.bucket:
            print most_sign_bits(s)
    
    def find_closest_node(self, node_id):
        # If we have no known nodes, exception!
        if len(self._nodes) == 0:
            raise RuntimeError, "No nodes in routing table!"