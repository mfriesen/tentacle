import socket
import struct
import sys

from tentacle.shared.discovery import Discovery

class ScreedResponse(object):
    
    screed = None
    server = None
    
    def __init__(self, screed, server):
        self.screed = screed
        self.server = server
        
class MulticastDiscovery(Discovery):
    
    sock = None
    multicast_group = None
    
    def start(self):
        print 'starting 1....'
        self.multicast_group = ('224.3.29.71', 10000)

        # Create the datagram socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout so the socket does not block indefinitely when trying
        # to receive data.
        self.sock.settimeout(0.2)

        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment.
        ttl = struct.pack('b', 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def send_message(self, screed):
        # Send data to the multicast group
        message = screed.to_json()
        print >>sys.stderr, 'sending "%s"' % message
        self.sock.sendto(message, self.multicast_group)
        
        responses = list()

        # Look for responses from all recipients
        while True:
            print >>sys.stderr, 'waiting to receive'
            try:
                data, server = self.sock.recvfrom(65565)
            except socket.timeout:
                print >>sys.stderr, 'timed out, no more responses'
                break
            else:
                responses.append(ScreedResponse(screed, server))
                print >>sys.stderr, 'received!!! "%s" from %s' % (data, server)

        return responses
        
    def stop(self):
        print >>sys.stderr, 'closing socket'
        self.sock.close()