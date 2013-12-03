import json

class Screed(object):
    
    STATUS_SUCCESS = "success"
    STATUS_FAIL = "fail"
    STATUS_ERROR = "error"

    screed = None
    status = None
    
    def __init__(self):
        self.screed = dict()
    
    '''
    Add command to screed
    Returns index of command added
    '''
    def add_cmd(self, cmd):
        if 'cmds' not in self.screed:
            self.screed['cmds'] = list()
        
        comp = dict({'cmd': cmd})
        self.screed['cmds'].append(comp)
        return len(self.screed['cmds']) - 1

    '''
    Add result to command
    Requires index > -1
    '''
    def add_result(self, index = -1, text = ''):
        if index > -1:
            dic = dict({'text': text})            
            self.cmds()[index]['result'] = dic 

    '''
    Add status to command
    Requires index > -1
    '''
    def add_status(self, index = -1, status = None):
        if index > -1: 
            self.cmds()[index]['status'] = status 
            
    '''
    Returns commands on screed
    '''
    def cmds(self):
        if 'cmds' in self.screed:
            return self.screed['cmds']
        return list()  
    
    def cmd(self, index = -1):
        if index > -1:
            return self.cmds()[index]['cmd']
        return ''
    #def dict(self):
    #    return self.screed
    
    '''
    loads screed from JSON data
    '''
    def load(self, json_data):
        self.screed = json.loads(json_data)['screed']
    
    '''
    Returns the result from the command at index
    '''
    def result(self, index = -1):
        if index > -1:
            return self.cmds()[index]['result']
        return ''
    
    '''
    Sets the status SUCCESS
    '''
    def status_success(self, index=None):
        if index is None:
            self.status = self.STATUS_SUCCESS
        else:
            self.add_status(index, self.STATUS_SUCCESS)

    '''
    Sets the status FAIL
    '''
    def status_fail(self, index=None):
        if index is None:
            self.status = self.STATUS_FAIL
        else:
            self.add_status(index, self.STATUS_FAIL)

    '''
    Sets the status ERROR
    '''
    def status_error(self, index=None):
        if index is None:
            self.status = self.STATUS_ERROR
        else:
            self.add_status(index, self.STATUS_ERROR)

    '''
    Returns a JSON representation of the Screed
    '''
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=0)