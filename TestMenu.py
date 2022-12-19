import unittest
from RecruitmentSystem.sub_system.menu import menu
from unittest.mock import patch

class TestMenu(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
        
    def setUp(self):
        self.m=menu()
        
    def tearDown(self):
        pass
    
    
    @patch("menu.inputs")
    def test_login(self,mock_input):
        
        mock_input.side_effect=['1','j1','1']
        self.assertEqual(self.m.login(),(True, 1, jobseeker))
        
        mock_input.side_effect=['1','j1','2']
        self.assertEqual(self.m.login(),(False, 1, None))
        
        mock_input.side_effect=['2','Admin1','1']
        self.assertEqual(self.m.login(),(True, 2, Admin))
        
        mock_input.return_value='3'
        self.assertEqual(self.m.login(),(False, None, None))
        
    @patch("menu.inputs2")    
    def test_search_company(self,mock_input):
        
        mock_input.return_value='Amazon'
        self.assertEqual(self.m.search_company(),'Amazon')
        
        mock_input.return_value='Google'
        self.assertEqual(self.m.search_company(),'Google')
        
        mock_input.return_value='Facebook'
        self.assertFalse(self.m.search_company())
        
        mock_input.return_value='Microsoft'
        self.assertFalse(self.m.search_company())
        
unittest.main(argv=[''], verbosity=2, exit=False)
        
        
        
    