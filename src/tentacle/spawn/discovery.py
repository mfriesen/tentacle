import socket
import struct

from tentacle.spawn.operation import run_screed

class Discovery(object):
        
    def start(self):
        pass
    
    def listen_for_message(self, spawnConfig):
        pass
        
    def stop(self):
        pass

class MulticastDiscovery(Discovery):
    
    sock = ""
    
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
            
    def listen_for_message(self, spawnConfig):
                    
        try:
            data, address = self.sock.recvfrom(1024)
    
            ack = run_screed(spawnConfig, data)

            self.sock.sendto(ack, address)

        except:
            pass

    def stop(self):
        self.sock.close()