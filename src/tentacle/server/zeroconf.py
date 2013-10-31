import select
import pybonjour
import threading

def singleton(cls):
    return cls()

@singleton
class Zeroconf(object):
    
    count = 0
    timeout  = 5
    resolved = []

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.count = 0
        
    def pybonjour(self):
        
        self.lock.acquire()
        
        try:
            print 'running '
            print self.count
            self.count = self.count + 1
        finally:
            self.lock.release()

    def resolve_callback(self, sdRef, flags, interfaceIndex, errorCode, fullname, hosttarget, port, txtRecord):
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            print 'Resolved service:'
            print '  fullname   =', fullname
            print '  hosttarget =', hosttarget
            print '  port       =', port
            self.resolved.append(True)

    def browse_callback(self, sdRef, flags, interfaceIndex, errorCode, serviceName, regtype, replyDomain):
        print 'browse_callback'
        if errorCode != pybonjour.kDNSServiceErr_NoError:
            return

        if not (flags & pybonjour.kDNSServiceFlagsAdd):
            print 'Service removed'
            return

        print 'Service added; resolving'

        resolve_sdRef = pybonjour.DNSServiceResolve(0,
                                                interfaceIndex,
                                                serviceName,
                                                regtype,
                                                replyDomain,
                                                self.resolve_callback)

        try:
            while not self.resolved:
                ready = select.select([resolve_sdRef], [], [], self.timeout)
                if resolve_sdRef not in ready[0]:
                    print 'Resolve timed out'
                    break
                pybonjour.DNSServiceProcessResult(resolve_sdRef)
            else:
                self.resolved.pop()
        finally:
            resolve_sdRef.close()

    def querySpawns(self):
        
        browse_sdRef = pybonjour.DNSServiceBrowse(regtype = '_test._tcp', callBack = self.browse_callback)
        pybonjour.DNSServiceProcessResult(browse_sdRef)
        
def querySpawns():
    #Zeroconf.pybonjour()
    Zeroconf.querySpawns()