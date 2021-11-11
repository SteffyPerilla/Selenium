import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2) 