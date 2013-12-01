from tentacle.shared import Screed
from tentacle.cthulhu.model import CthulhuData
    
def querySpawns():
    print 'querying for spawns....'
    
    screed = Screed("hello")
    response = CthulhuData.send_message(screed)
    print '------------ response start --------------------------'
    print response.server
    print response.status
    print response.message
    print '------------ response end --------------------------'
    #Zeroconf.querySpawns()
    
def sendTestMessage():
    response = CthulhuData.send_message(Screed('this is our awesome message'))
    print '------------ response start --------------------------'
    print response.server
    print response.status
    print response.message
    print '------------ response end --------------------------'