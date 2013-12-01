import json
import uuid
import socket

spawn_id = uuid.uuid4()

def to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=0)

class ScreedResult(object):
    os = ""
    name = ""
    address = ""
    port = ""
    text = ""
    
class Screed(object):
    
    STATUS_SUCCESS = "success"
    STATUS_FAIL = "fail"
    STATUS_ERROR = "error"
    
    spawn_id = None
    status = None
    cmd = None
    result = None
    cmds = None
    
    def __init__(self, cmd = None):
        
        if cmd is not None:
            self.cmd = cmd
        else:
            self.spawn_id = str(spawn_id)
        
    def status_success(self):
        self.status = self.STATUS_SUCCESS

    def status_fail(self):
        self.status = self.STATUS_FAIL

    def status_error(self):
        self.status = self.STATUS_ERROR
                
    def add_result(self):
        self.result = ScreedResult()
        return self.result
    
    def add_cmd(self, cmd):
        if self.cmds is None:
            self.cmds = list()
        screed = Screed(cmd)
        self.cmds.append(screed)
        return screed
'''
class HelloScreed(Screed):
    id = ""
    name = ""
    address = ""
    port = ""
    os = ""    

    def __init__(self):
        self.id = str(spawn_id)
        self.name = socket.gethostname()
        self.address = socket.gethostbyname(socket.gethostname())
        self.port = ""    

class Host(object):
    id = spawn_id
    name = socket.gethostname()
    address = socket.gethostbyname(socket.gethostname())
    port = ""
    
class Action(object):
    
    action = ""
    value = ""
    host = Host()
    
    def __init__(self, action="", value=""):
        self.action = action
        self.value = value
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=0)
        
class ActionResponse(object):
    STATUS_NEW = 3
    STATUS_TIMEOUT = 2
    STATUS_SUCCESS = 1
    status = STATUS_NEW
    message = ''
    server = ''
    
'''