import json
from tentacle.shared import Action
from pprint import pprint

def action_response(action_json):
    
    resp = 'ack'
    data = json.loads(action_json)
    action = data['action']
    
    if (action == 'hello'):
        print 'sending hello response'
        action = Action("hello")
        resp = action.to_JSON()
        print '---------'
        print resp
        print type(resp)
        print '---------'
        
    return resp