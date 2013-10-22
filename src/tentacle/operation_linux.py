from tentacle.operation import Operation

class OperationLinux(Operation):
        
    def service_start_args(self, service_name):
        return ["/usr/sbin/service", service_name, "start"]
    
    def service_stop_args(self, service_name):
        return ["/usr/sbin/service", service_name, "stop"]