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
        
        steps = self.steps()
        
        if (step == len(steps)):
            steps.insert(step, dict())
        elif (step >= len(steps)):
            for i in range(len(steps), step + 1):
                steps.insert(i, dict())
            
        self.step(step).update({fn_name : fn})
    
    '''
    Gets the functions in a step
    '''
    def step(self, step):
        return self.steps()[step] 
    
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