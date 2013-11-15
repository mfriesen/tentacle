import select
import socket
import pybonjour
from tentacle.settings import DEFAULT_BONJOUR_REGTYPE
from tentacle.spawn import Spawn

def singleton(cls):
    return cls()

@singleton
class Zeroconf(object):
    
    timeout  = 5
    spawns = {}

    def __init__(self):
        pass

    def spawn_add(self, fullname, hosttarget, port):
        spawn = Spawn(fullname, hosttarget, port, socket.gethostbyname(hosttarget))
        self.spawns[fullname] = spawn
#        print '----------- adding -------------------'
#        print '  fullname   =', spawn.fullname
#        print '  hosttarget =', spawn.hosttarget
#        print '  port       =', spawn.port
#        print '  ipaddress  =', spawn.ipaddress
#        print ' list size '
#        print len(self.spawns)
        
    def spawn_list(self):
        return self.spawns
        
    def resolve_callback(self, sdRef, flags, interfaceIndex, errorCode, fullname, hosttarget, port, txtRecord):
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            self.spawn_add(fullname, hosttarget, port)

    def browse_callback(self, sdRef, flags, interfaceIndex, errorCode, serviceName, regtype, replyDomain):
        
        if errorCode != pybonjour.kDNSServiceErr_NoError:
            return

        if not (flags & pybonjour.kDNSServiceFlagsAdd):
#            print 'Service removed'
            return

        resolve_sdRef = pybonjour.DNSServiceResolve(0,
                                                interfaceIndex,
                                                serviceName,
                                                regtype,
                                                replyDomain,
                                                self.resolve_callback)
        try:
            ready = select.select([resolve_sdRef], [], [], self.timeout)
            if resolve_sdRef in ready[0]:
                pybonjour.DNSServiceProcessResult(resolve_sdRef)
            else:
#                print 'Resolve timed out'
                pass
        finally:
            resolve_sdRef.close()

    def querySpawns(self):        
        browse_sdRef = pybonjour.DNSServiceBrowse(regtype = DEFAULT_BONJOUR_REGTYPE, callBack = self.browse_callback)
        pybonjour.DNSServiceProcessResult(browse_sdRef)
                
def querySpawns():
    Zeroconf.querySpawns()