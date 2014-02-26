import os
import hashlib
import logging

import socket
import sys
import base64
import struct

from bencode import bencode, bdecode
from tentacle.dht.dht_bucket_routing_table import DHTBucketRoutingTable
from tentacle.dht.routing_table import DHTRoutingTable

# See http://docs.python.org/library/logging.html
logger = logging.getLogger(__name__)

class DHTRequest(object):
    
    def __init__(self, host, port, data):
        self.host = host
        self.port = port
        self.data = data

class DHTResponse(dict):
    
    def __init__(self, response):

        rec = bdecode(response)
        self.update(rec)
        logger.debug(self)
        
    def transaction_id(self):
        return self['t']
    
    def is_response(self):
        return self['y'] == 'r'
    
    def is_query(self):
        return self['y'] == 'q' 
    
    def is_error(self):
        return self['y'] == 'e'
    
    def response_dic(self):
        return self['r']
        
class DHT(object):
    
    def __init__(self, id_, routing_table  = None, default_host="router.bittorrent.com", default_port=6881):
        self._id = id_
        self._default_host = default_host
        self._default_port = default_port
        
        if routing_table is None:
            routing_table = DHTBucketRoutingTable(self._id)
            
        self._routing_table = routing_table
    
    """
    sends ping request for an Node
    """
    def ping(self):
        q = { "t" : "aa", "y":"q", "q" : "ping", "a":{"id":self._id}}
        request = DHTRequest(self._default_host, self._default_port, bencode(q))
        response = self.send_request(request)
        return response
 
    """
    convert long int to dotted quad string
    """
    def numToDottedQuad(self, n):
        d = 256 * 256 * 256
        q = []
        while d > 0:
            m, n = divmod(n, d)
            q.append(str(m))
            d /= 256

        return '.'.join(q)

    """
    Decode node_info into a list of id, connect_info
    """
    def decode_nodes(self, nodes):
        nrnodes = len(nodes) / 26        
        nodes = struct.unpack("!" + "20sIH" * nrnodes, nodes)
        for i in xrange(nrnodes):
            id_, ip, port = nodes[i * 3], self.numToDottedQuad(nodes[i * 3 + 1]), nodes[i * 3 + 2]
            self._routing_table.add_node(id_)
            print "id_ " , base64.b64encode(id_) , "IP " , ip , " PORT ", port
            #self.strxor(self._id, id_)
            #print self.node_distance(self._id, id_)

    """
    sends find_node request to network
    """
    def find_node(self, node_id):
        q = {"t":"aa", "y":"q", "q":"find_node", "a":{"id":self._id, "target":node_id}}
        request = DHTRequest(self._default_host, self._default_port, bencode(q))
        response = self.send_request(request)
        
        #v = response.response_dic()['nodes']
        #self.decode_nodes(v)
        return response
    
    """
    calculates the distance between 2 nodes
    """
    def node_distance(self, id1, id2):
        return int(hashlib.sha1(id1).hexdigest(), 16) ^ int(hashlib.sha1(id2).hexdigest(), 16)
        
    def send_request(self, request):
        
        socket = self.__create_socket__()
            
        response = self.__send_request__(socket, request)
        
        return response
    
    def __create_socket__(self):
        try:
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)            
        except socket.error:
            raise 'Failed to create socket'
    
    def __send_request__(self, socket, request):
        try :
            socket.sendto(request.data, (request.host, request.port))
    
            # receive data from client (data, addr)
            d = socket.recvfrom(1024)
            reply = d[0]
            #addr = d[1]
         
            return DHTResponse(reply)
     
        except socket.error, msg:
            raise 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        
if __name__ == "__main__":
    
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    
    dht = DHT(id_=hashlib.sha1("this salts the ID TODO change this").digest())
    
    #print dht1.get_peers("8ac3731ad4b039c05393b5404afa6e7397810b41".decode("hex"))
    #dht1.ping()