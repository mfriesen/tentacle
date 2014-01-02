import unittest
 
from tentacle.cthulhu.datastore import Datastore
from tentacle.shared.screed import Screed

class TestDatastore(unittest.TestCase):
        
    def setUp(self):
        pass
    
    def create_screed(self):
        # given        
        screed = Screed()
        screed.name("Name")
        screed.description("Description")
        screed.typeValue("Python")

        result = Datastore.save_screed(screed)
        
        return result;
        
    def test_save_01(self):
        # given
        
        # when
        result = self.create_screed()
        
        # then
        self.assertTrue(result.id > 0)

    # find saved screed        
    def test_get_01(self):
        # given        
        base = self.create_screed()
        
        # when
        result = Datastore.get_screed(base.id)
        
        # then
        expect = '{\n"screed": {\n"description": "Description", \n"name": "Name", \n"steps": [], \n"type": "Python"\n}\n}'
        self.assertEqual(expect, result.to_json())

    # find screed, not found        
    def test_get_02(self):
        # given
        
        # when
        result = Datastore.get_screed(30203349)
        
        # then
        self.assertTrue(result is None)

if __name__ == '__main__':
    unittest.main()