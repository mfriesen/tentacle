import hashlib

def byte_to_int(bytes_):
    hex_ = ''.join( [ "%02X" % ord(b) for b in bytes_ ] )
    return int(hex_, 16)

def sha1_id(string):
    return int(hashlib.sha1(string).hexdigest(), 16)

def to_binary(s):
    
    if isinstance(s, basestring):
        return ''.join(format(x, '008b') for x in bytearray(s))
    
    return "{00:b}".format(s).zfill(len(str(s)) * 4)

def distance(s1, s2):
    print s1 , " " , s2
    return int(s1) ^ int(s2)    


class DHTNode(object):
    
    def __init__(self, id_, host, port):
        self._id = id_
        self._host = host
        self._port = port    

class DHTRoutingTable(object):
    
    def add_node(self, dhtNode):
        raise NotImplemented
        
    def find_closest_nodes(self, node_id):
        raise NotImplemented
