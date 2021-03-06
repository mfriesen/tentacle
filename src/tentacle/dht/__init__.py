import os
import hashlib
import logging

import socket
import sys
import base64
import struct

from bencode import bencode, bdecode
from tentacle.dht.dht_bucket_routing_table import DHTBucketRoutingTable
from tentacle.dht.routing_table import DHTRoutingTable, DHTNode, byte_to_int

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
    
    def data(self):
        return self['r']

class DHT(object):
    
    def __init__(self, id_, routing_table  = None):
        self._id = id_
        
        if routing_table is None:
            routing_table = DHTBucketRoutingTable(self._id)
            
        self._routing_table = routing_table        
    
    def add_nodes_default(self):
        
        # localhost
        host = socket.gethostbyname(socket.gethostname())
        self.add_node(host, 1111, self._id) # TODO get proper IP

        # router.bittorrent.com
        self.add_node("67.215.242.138", 6881)
    
    """
    add nodes to DHT
    """
    def add_node(self, host, port, id_ = None):
        
        if id_ is None:
            response = self.ping(host, port)
        
            if response.is_response():
                self._routing_table.add_node(DHTNode(response.data()['id'], host, port))
        else:
            self._routing_table.add_node(DHTNode(id_, host, port))

    
    """
    sends ping request for an Node
    """
    def ping(self, host, port):
        q = { "t" : "aa", "y":"q", "q" : "ping", "a":{"id":self._id}}
        request = DHTRequest(host, port, bencode(q))
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
    Decodes data from "find_node" response and adds nodes to routing table
    """
    def __add_nodes_from_find_node_response(self, response):
        if response.is_response():
            nodes = response.data()['nodes']
                    
            nrnodes = len(nodes) / 26        
            nodes = struct.unpack("!" + "20sIH" * nrnodes, nodes)
        
            for i in xrange(nrnodes):            
                id_, host, port = byte_to_int(nodes[i * 3]), self.numToDottedQuad(nodes[i * 3 + 1]), nodes[i * 3 + 2]
                self.add_node(host, port, id_)

    """
    sends find_node request to network
    """
    def find_closest_nodes(self, node_id):
        
        nodes = list()
        bucket = self._routing_table.find_closest_nodes(node_id)
        
        # look for node_id in returned list
        for s in bucket._nodes:
            if s == node_id:
                dhtNode = bucket._nodes[s]
                nodes.append(dhtNode)
                return nodes
                
        for s in bucket._nodes:
            if s != node_id:
                dhtNode = bucket._nodes[s]
                q = {"t":"aa", "y":"q", "q":"find_node", "a":{"id":self._id, "target":s}}
                request = DHTRequest(dhtNode._host, dhtNode._port, bencode(q))
                response = self.send_request(request)
        
                self.__add_nodes_from_find_node_response(response)
        
        bucket = self._routing_table.find_closest_nodes(node_id)
        return bucket.values()
            
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