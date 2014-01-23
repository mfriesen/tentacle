import os
import hashlib
import logging

import socket
import sys
import base64

from bencode import bencode, bdecode

# See http://docs.python.org/library/logging.html
logger = logging.getLogger(__name__)

class DHTRequest(object):
    
    def __init__(self, host, port, data):
        self.host = host
        self.port = port
        self.data = data

class DHTResponse(dict):
    
    def __init__(self, response):
        self.update(bdecode(response))
        print self
        
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
    
    def __init__(self, id_, default_host="router.bittorrent.com", default_port=6881):
        print "id ", base64.b64encode(id_)
        self._id = id_
        self._default_host = default_host
        self._default_port = default_port
    
    """
    sends ping request for an Node
    """
    def ping(self):
        q = { "t" : "aa", "y":"q", "q" : "ping", "a":{"id":self._id}}
        request = DHTRequest(self._default_host, self._default_port, bencode(q))
        #response = self.send_request(request)
        reply = "d1:rd2:id20:mnopqrstuvwxyz123456e1:t2:aa1:y1:re"   
        response = DHTResponse(reply)
        return response
 
    """
    sends find_node request to network
    """
    def find_node(self, node_id):
        q = {"t":"aa", "y":"q", "q":"find_node", "a":{"id":self._id, "target":node_id}}
        request = DHTRequest(self._default_host, self._default_port, bencode(q))
        #response = self.send_request(request)
        reply = "d1:rd2:id20:0123456789abcdefghij5:nodes9:def456...e1:t2:aa1:y1:re"   
        response = DHTResponse(reply)
        return response
    
    def send_request(self, request):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
        except socket.error:
            raise 'Failed to create socket'
            
        try :
            # TODO mock...
            s.sendto(request.data, (request.host, request.port))
    
            # receive data from client (data, addr)
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
         
            print 'Server reply : ' + reply + " from address " , addr[0] , " port " ,addr[1]
               
            return DHTResponse(reply)
     
        except socket.error, msg:
            raise 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            
if __name__ == "__main__":
    
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    
    dht = DHT(id_=hashlib.sha1("this salts the ID TODO change this").digest())
    
    #print dht1.get_peers("8ac3731ad4b039c05393b5404afa6e7397810b41".decode("hex"))
    #dht1.ping()