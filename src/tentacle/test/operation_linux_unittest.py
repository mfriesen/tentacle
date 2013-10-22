import unittest

from tentacle.operation_linux import OperationLinux

class TestOperationLinux(unittest.TestCase):
    
    operation = OperationLinux()
    
    def setUp(self):
        pass
    
    def test_service_start_args01(self):
        
        array = self.operation.service_start_args("Tomcat")
        self.assertEqual(3, len(array))
        self.assertEqual("/usr/sbin/service", array[0])
        self.assertEqual("Tomcat", array[1])
        self.assertEqual("start", array[2])

    def test_service_stop_args01(self):
        
        array = self.operation.service_stop_args("Tomcat")
        self.assertEqual(3, len(array))
        self.assertEqual("/usr/sbin/service", array[0])
        self.assertEqual("Tomcat", array[1])
        self.assertEqual("stop", array[2])
    
if __name__ == '__main__':
    unittest.main()