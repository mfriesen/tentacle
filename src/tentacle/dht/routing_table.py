
def most_sign_bits(s):
    
    if isinstance(s, basestring):
        return ''.join(format(x, '008b') for x in bytearray(s))
    
    return "{00:b}".format(s).zfill(len(str(s)) * 4)

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
