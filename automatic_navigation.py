import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep 

class NavigationAutomatic(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com')
    
    def test_browser_navigation(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,testRunner= HTMLTestRunner(output='Report', report_name='automatic_navigation_report'))        

