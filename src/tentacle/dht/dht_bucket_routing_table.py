from tentacle.dht.routing_table import DHTRoutingTable, distance
from math import pow

MAX_BUCKET_SIZE = 8

class DHTBucket(object):

    def __init__(self):
        self._nodes = dict()

    def add_node(self, dhtNode):
        self._nodes[dhtNode._id] = dhtNode

    def is_bucket_full(self):
        return len(self._nodes) >= MAX_BUCKET_SIZE
    
    def is_empty(self):
        return len(self._nodes) == 0
    
    def values(self):
        return self._nodes.values()
    
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
        
    def add_node(self, dhtNode):
        self._bucket.add_node(dhtNode)
        
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
        bucketNode = DHTBucketNode(min_ = min_, max_ = max_)
        return bucketNode
    
    def add_node(self, dhtNode):

        bucketNode = self.__find_bucket__(self._root, dhtNode)
        bucketNode.add_node(dhtNode)
        
        if bucketNode.is_bucket_full():
            self.__split_bucket__(bucketNode)
    
    def __find_bucket__(self, bucketNode, dhtNode):
         
        if bucketNode is not None and bucketNode.is_node_id_within_bucket(dhtNode._id):
            
            if bucketNode._left is not None and bucketNode._left.is_node_id_within_bucket(dhtNode._id):
                bucketNode = self.__find_bucket__(bucketNode._left, dhtNode)

            if bucketNode._right is not None and bucketNode._right.is_node_id_within_bucket(dhtNode._id):
                bucketNode = self.__find_bucket__(bucketNode._right, dhtNode)

        return bucketNode
        
    def __split_bucket__(self, bucketNode):
        
        if bucketNode.is_bucket_full():

            half = (bucketNode._max - bucketNode._min) / 2
            left_node = self.__create_node__(bucketNode._min, bucketNode._min + half)
            right_node = self.__create_node__(bucketNode._min + half + 1, bucketNode._max)
            
            for node_id in bucketNode._bucket._nodes:
                
                dhtNode = bucketNode._bucket._nodes[node_id]
                if right_node.is_node_id_within_bucket(dhtNode._id):
                    right_node.add_node(dhtNode)
                elif left_node.is_node_id_within_bucket(dhtNode._id):
                    left_node.add_node(dhtNode)
            
            if not left_node._bucket.is_empty() and not right_node._bucket.is_empty() and bucketNode.is_node_id_within_bucket(self._id):
                bucketNode._bucket = None
                bucketNode._left = left_node
                bucketNode._right = right_node

                self.__split_bucket__(left_node)
                self.__split_bucket__(right_node)

            else: # only keep the closest nodes
                bucketNode._bucket.truncate(self._id)
                    
    def find_closest_nodes(self, id_):        
        bucket = DHTBucket()
        self.__find_closest_nodes__(self._root, bucket, id_)
        return bucket
            
    def __find_closest_nodes__(self, bucketNode, bucket, id_):
        
        if bucketNode is not None and bucketNode.is_node_id_within_bucket(id_):
            self.__find_closest_nodes__(bucketNode._left, bucket, id_)
            self.__find_closest_nodes__(bucketNode._right, bucket, id_)
            
            if bucketNode._bucket is not None and not bucket.is_bucket_full():
                for node_id in bucketNode._bucket._nodes:
                    dhtNode = bucketNode._bucket._nodes[node_id]
                    bucket.add_node(dhtNode)
                
                bucket.truncate(id_)
                
                
