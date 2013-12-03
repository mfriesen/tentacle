from tentacle.shared.screed import Screed

def process_operation(json_data):
    
    screed = Screed()
    screed.load(json_data)
    
    for index in range(len(screed.cmds())):
        cmd = screed.cmd(index)
        
        if cmd == 'hello':
            screed.add_result(index, text = "everything is good...")
            screed.status_success(index)
    
    screed.status_success()
    return screed.to_json()