from tentacle.operation import Operation

class OperationMac(Operation):
    
    def service_start_args(self, service_name):
        return ["launchctl", "start", service_name]
    
    def service_stop_args(self, service_name):
        return ["launchctl", "stop", service_name]