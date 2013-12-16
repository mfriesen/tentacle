import json

class Screed(dict):
    
    STATUS_SUCCESS = "success"
    STATUS_FAIL = "fail"
    STATUS_ERROR = "error"

    screed = None
    status = None
    
    def __init__(self):
        self.screed = dict()
        self.update({"screed" : list()})
    
    '''
    Add function to a step
    '''
    def add_fn(self, step, fn_name, fn):
        screed = self.get("screed")
        
        if (step == len(screed)):
            screed.insert(step, dict())
        elif (step >= len(screed)):
            for i in range(len(screed), step + 1):
                screed.insert(i, dict())
            
        self.get("screed")[step].update({fn_name : fn})

    '''
    Return steps in screed
    '''
    def steps(self):
        return self.get("screed")
    
    '''
    Add status to step
    Requires step > -1
    '''
    def add_status(self, step = -1, status = None):
        if step > -1: 
            self.get("screed")[step].update({"status" : status})
    
    '''
    loads screed from JSON data
    '''
    def load(self, json_data):
        self.update(json.loads(json_data))
    
    '''
    Sets the status SUCCESS
    '''
    def status_success(self, index=None):
        if index is None:
            self.status = self.update({"status" : self.STATUS_SUCCESS})
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