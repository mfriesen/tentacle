import unittest
from mock import patch
from tentacle.operation_linux import OperationLinux

class TestOperationLinux(unittest.TestCase):
    
    operation = OperationLinux()
    
    def setUp(self):
        pass
    
    def test_service_start_args01(self):
        
        result = self.operation.service_start_args("Tomcat")
        self.assertEqual(3, len(result))
        self.assertEqual("/usr/sbin/service", result[0])
        self.assertEqual("Tomcat", result[1])
        self.assertEqual("start", result[2])

    def test_service_stop_args01(self):
        
        result = self.operation.service_stop_args("Tomcat")
        self.assertEqual(3, len(result))
        self.assertEqual("/usr/sbin/service", result[0])
        self.assertEqual("Tomcat", result[1])
        self.assertEqual("stop", result[2])
    
    # succussfully stop service
    @patch.object(OperationLinux, 'perform_subprocess')
    def test_service_stop01(self, mock_perform_subprocess):
        mock_perform_subprocess.return_value=('vsftpd stop/waiting', '')
        result = self.operation.service_stop("vsftpd")
        self.assertEqual('vsftpd stop/waiting', result.stdoutdata)
        self.assertTrue(result.isSuccess())
        self.assertEqual('', result.stderrdata)
      
    # unsuccussful stop service
    @patch.object(OperationLinux, 'perform_subprocess')
    def test_service_stop02(self, mock_perform_subprocess):
        mock_perform_subprocess.return_value=('', 'vsftpd: unrecognized service')
        result = self.operation.service_stop("vsftpd")
        self.assertEqual('', result.stdoutdata)
        self.assertFalse(result.isSuccess())
        self.assertEqual('vsftpd: unrecognized service', result.stderrdata)
          
if __name__ == '__main__':
    unittest.main()