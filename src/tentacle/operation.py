import subprocess

class Operation:

    def __init__(self):
        pass
    
    def service_start_args(self, service_name):
        pass
    
    def service_stop_args(self, service_name):
        pass
    
    def perform_operation(self, args):
        p = subprocess.Popen(args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        return p.communicate()
    
    def service_start(self, service_name):
        return self.perform_operation(self.service_start_args(service_name)) 
    
    def service_stop(self, service_name):
        return self.perform_operation(self.service_stop_args(service_name))
    
    def service_restart(self, service_name):
        self.service_stop(service_name)
        self.service_start(service_name)