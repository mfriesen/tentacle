from tentacle.dht.routing_table import DHTRoutingTable, distance
from math import pow

MAX_BUCKET_SIZE = 8

class DHTBucket(object):

    def __init__(self):
        self._nodes = dict()

    def add_node(self, id_):
        self._nodes[id_] = id_

    def is_bucket_full(self):
        return len(self._nodes) >= MAX_BUCKET_SIZE
    
    def is_empty(self):
        return len(self._nodes) == 0
    
    def truncate(self, compare_node_id):
        if len(self._nodes) > MAX_BUCKET_SIZE:
            distance_map = dict()
            
            for s in self._nodes:
                distance_map[distance(compare_node_id, s)] = s

            l = sorted(distance_map)
                
            for i in range(0, len(self._nodes) - MAX_BUCKET_SIZE):
                del self._nodes[distance_map[l[i]]]

        
class DHTBucketNode(object):
    
    def __init__(self, min_, max_):
        self._bucket = DHTBucket()
        self._min = int(min_)
        self._max = int(max_)
        self._left = None
        self._right = None
        
    def add_node(self, id_):
        self._bucket.add_node(id_)
        
    def is_bucket_full(self):
        return self._bucket.is_bucket_full()
    
    def is_node_id_within_bucket(self, node_id):
        return (self._min < node_id) and (node_id <= self._max)        

class DHTBucketRoutingTable(DHTRoutingTable):
    
    _root = None
    
    def __init__(self, id_):
        self._root = DHTBucketNode(min_ = 0, max_ = pow(2, 160))        
        self._id = id_
    
    def __create_node__(self, min_, max_):
        node = DHTBucketNode(min_ = min_, max_ = max_)
        return node
    
    def add_node(self, node_id):

        node = self.__find_bucket__(self._root, node_id)
        node.add_node(node_id)
        
        if node.is_bucket_full():
            self.__split_bucket__(node)
    
    def __find_bucket__(self, node, node_id):
         
        if node is not None and node.is_node_id_within_bucket(node_id):
            
            if node._left is not None and node._left.is_node_id_within_bucket(node_id):
                node = self.__find_bucket__(node._left, node_id)

            if node._right is not None and node._right.is_node_id_within_bucket(node_id):
                node = self.__find_bucket__(node._right, node_id)

        return node
        
    def __split_bucket__(self, node):
        
        if node.is_bucket_full():

            half = (node._max - node._min) / 2
            left_node = self.__create_node__(node._min, node._min + half)
            right_node = self.__create_node__(node._min + half + 1, node._max)
            
            for s in node._bucket._nodes:
                
                if right_node.is_node_id_within_bucket(s):
                    right_node.add_node(s)
                elif left_node.is_node_id_within_bucket(s):
                    left_node.add_node(s)
            
            if not left_node._bucket.is_empty() and not right_node._bucket.is_empty() and node.is_node_id_within_bucket(self._id):
                node._bucket = None
                node._left = left_node
                node._right = right_node

                self.__split_bucket__(left_node)
                self.__split_bucket__(right_node)

            else: # only keep the closest nodes
                node._bucket.truncate(self._id)
                    
    def find_closest_nodes(self):        
        bucket = DHTBucket()
        self.__find_closest_nodes__(self._root, bucket)
        return bucket
            
    def __find_closest_nodes__(self, node, bucket):
        
        if node is not None and node.is_node_id_within_bucket(self._id):
            self.__find_closest_nodes__(node._left, bucket)
            self.__find_closest_nodes__(node._right, bucket)
            
            if not bucket.is_bucket_full():
                for s in node._bucket._nodes:
                    bucket.add_node(s)
                
                bucket.truncate(self._id)
                
                
