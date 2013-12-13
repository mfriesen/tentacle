import sys
import StringIO

from tentacle.shared.screed import Screed

def run_operation():
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    #exec("for v in ['cat', 'window', 'defenestrate']:\n\tprint v\n")
    exec("import socket\nprint socket.gethostname()")
    sys.stdout = old_stdout

    print redirected_output.getvalue()
        
def process_operation(json_data):
    
    screed = Screed()
    screed.load(json_data)
    
    for index in range(len(screed.cmds())):
        cmd = screed.cmd(index)
        
        if cmd == 'hello':
            #import socket
            #os = ""
            #name = ""
            #address = ""
            #port = ""
            #text = ""
            #self.name = socket.gethostname()
            #self.address = socket.gethostbyname(socket.gethostname())

            screed.add_result(index, text = "everything is good...")
            screed.status_success(index)
    
    screed.status_success()
    return screed.to_json()