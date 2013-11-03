
class Spawn(object):
    
    fullname = ""
    hosttarget = ""
    port = ""
    ipaddress = ""
    
    def __init__(self, fullname, hosttarget, port, ipaddress):
        self.ipaddress = ipaddress
        self.fullname = fullname
        self.hosttarget = hosttarget
        self.port = port
    