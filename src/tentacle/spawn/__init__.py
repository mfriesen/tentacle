import os, time, sys
import threading, Queue

from tentacle.settings import *
from tentacle.spawn.discovery import MulticastDiscovery

class SpawnThread(threading.Thread):
    
    def __init__(self):
        super(SpawnThread, self).__init__()
        self.stoprequest = threading.Event()

    def run(self):

        discovery = MulticastDiscovery()
        discovery.start()

        while not self.stoprequest.isSet():
            discovery.listen_for_message()

    def join(self, timeout=None):
        self.stoprequest.set()
        super(SpawnThread, self).join(timeout)
        
def startSpawn(name = DEFAULT_BONJOUR_NAME, regtype = DEFAULT_BONJOUR_REGTYPE, port = DEFAULT_BONJOUR_PORT):
    print >>sys.stderr, 'starting spawn...'
    spawn = SpawnThread()
    spawn.start()

    try:
        print >>sys.stderr, '\nwaiting to receive message'
        while not spawn.stoprequest.isSet():
            pass
    except KeyboardInterrupt:
        spawn.join()
        print >>sys.stderr, '\n\nshutting down spawn...\n'