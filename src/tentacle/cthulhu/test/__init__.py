import unittest
 
from tentacle.cthulhu import ScreedRoot

class TestCthulhu(unittest.TestCase):
        
    def setUp(self):
        pass
    
    def create_screed(self):
        # given
        root = ScreedRoot()
        screedName = "Name"
        screedDescription = "Description"
        screedType = "Python"
        
        result = root.save(screedName, screedDescription, screedType)
        
        return result;
        
    def test_save_01(self):
        # given
        
        # when
        result = self.create_screed()
        
        # then
        self.assertEqual(1, result.id)
        
if __name__ == '__main__':
    unittest.main()