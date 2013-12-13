import os, time
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
            try:
                discovery.listen_for_message()
            finally:
                discovery.stop()
                print 'stopping thread'

    def join(self, timeout=None):
        self.stoprequest.set()
        super(SpawnThread, self).join(timeout)
        
def startSpawn(name = DEFAULT_BONJOUR_NAME, regtype = DEFAULT_BONJOUR_REGTYPE, port = DEFAULT_BONJOUR_PORT):
    spawn = SpawnThread()
    spawn.start()
    
    return spawn