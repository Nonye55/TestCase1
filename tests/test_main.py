import unittest
from page_objects.main import LampTrainees


class LT(unittest.TestCase):
    def setUp(self):
        self.driver = LampTrainees()
        self.driver.run_page()
        self.driver.login()

    def test_try_to_test(self):
        self.driver.invite_employee()
        
    def tearDown(self):
        self.driver.close_page()


if __name__ =='__main__':
    unittest.main()

