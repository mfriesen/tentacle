
def most_sign_bits(s, sig_bits):
    
    b = ''.join(format(x, 'b') for x in bytearray(s))
        
    if len(b) < sig_bits:
        b += ''.join(['0' for _ in range(0, sig_bits)])

    return b[:sig_bits]

def distance(s1, s2):
    s1 = str(s1)
    s2 = str(s2)
    
    if len(s1) != len(s2):
        raise Exception("distance cannot be calculated length " , len(s1) , " != ", len(s2))
    
    return int(''.join(str(ord(a) ^ ord(b)) for a,b in zip(s1,s2)))    


class DHTNode(object):
    
    def __init__(self, id_, host, port):
        self._id = id_
        self.host = host
        self.port = port    

class DHTRoutingTable(object):
    
    def add_node(self, node_id, node):
        raise NotImplemented
    
    def delete_node(self, node):
        raise NotImplemented
    
    def find_closest_node(self, node_id):
        raise NotImplemented

class DHTRoutingBucket(object):
    pass

class DHTRoutingBucketTable(DHTRoutingTable):
    
    def __init__(self):
        self._nodes = {}
    
    def add_node(self, node_id, node):
        self._nodes[node_id] = node
        
    def find_closest_node(self, node_id):
        # If we have no known nodes, exception!
        if len(self._nodes) == 0:
            raise RuntimeError, "No nodes in routing table!"