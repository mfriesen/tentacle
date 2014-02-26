import unittest
 
from tentacle.cthulhu.datastore import save_screed, ScreedBase, get_screed,\
    get_screeds, delete_screeds, delete_screed

class TestDatastore(unittest.TestCase):
        
    def setUp(self):
        delete_screeds()
    
    def create_screed(self):
        # given        
        base = ScreedBase(name="Name", description="Description", type="Python")
        result = save_screed(base)
        
        return result;
        
    def test_save_01(self):
        # given
        
        # when
        result = self.create_screed()
        
        # then
        self.assertTrue(result.id > 0)
        self.assertEquals("Name", result.name)

    # update screed
    def test_save_02(self):
        # given
        base = self.create_screed()
        base = get_screed(base.id)
        self.assertEquals("Name", base.name)
        base.name = "New Name"
        save_screed(base)
        
        # when
        result = get_screed(base.id)
        
        # then
        self.assertTrue(result.id > 0)
        self.assertEquals("New Name", result.name)

    # find saved screed        
    def test_get_screed01(self):
        # given        
        base = self.create_screed()
        
        # when
        result = get_screed(base.id)
        
        # then
        self.assertTrue(result is not None)
        #expect = '{\n"screed": {\n"description": "Description", \n"name": "Name", \n"steps": [], \n"type": "Python"\n}\n}'
        #self.assertEqual(expect, result.to_json())

    # find screed, not found        
    def test_get_screed02(self):
        # given
        
        # when
        result = get_screed(30203349)
        
        # then
        self.assertTrue(result is None)

    def test_get_screeds_01(self):
        # given        
        self.create_screed()

        # when
        result = get_screeds()
        
        # then
        self.assertEquals(1, len(result))
    
    def test_delete_screed_01(self):
        # given
        base = self.create_screed()
        
        # when
        delete_screed(base.id)
        
        # then
        self.assertIsNone(get_screed(base.id))
        
if __name__ == '__main__':
    unittest.main()