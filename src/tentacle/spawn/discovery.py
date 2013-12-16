import pybonjour
import socket
import struct
import select
import sys

from tentacle.spawn.operation import run_screed
from tentacle.settings import *
from tentacle.shared.discovery import Discovery

#def register_callback(sdRef, flags, errorCode, name, regtype, domain):
    #if errorCode == pybonjour.kDNSServiceErr_NoError:
        #print 'Registered service'
        #print '  name    =', name
        #print '  regtype =', regtype
        #print '  domain  =', domain
            
class MulticastDiscovery(Discovery):
    
    sock = ""
    #sdRef = ""
    
    def start(self):
        multicast_group = '224.3.29.71'
        
        server_address = ('', 10000)

        # Create the socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Bind to the server address
        self.sock.bind(server_address)
        
        # set port to non-blocking
        self.sock.setblocking(0)
    
        # Tell the operating system to add the socket to the multicast group
        # on all interfaces.
        group = socket.inet_aton(multicast_group)
        mreq = struct.pack('4sL', group, socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
        #self.sdRef = pybonjour.DNSServiceRegister(name = DEFAULT_BONJOUR_NAME,
        #                             regtype = DEFAULT_BONJOUR_REGTYPE,
        #                             port = DEFAULT_BONJOUR_PORT,
        #                             callBack = register_callback)
        
    def listen_for_message(self):
                    
        try:
            data, address = self.sock.recvfrom(1024)
    
            ack = run_screed(data)

            self.sock.sendto(ack, address)

        except:
            pass

    def stop(self):
        self.sock.close()
        #self.sdRef.close()