import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep

class MercadoLibrePage(unittest.TestCase):

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()
    
    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > button')
        order_menu.click()
        higher_price = driver.find_element_by_partial_link_text('Mayor precio')
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text 
            articles.append(article_name) 
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[1]/div/div/div[2]/div[2]/div[1]/div[1]/a/div/div/span[1]/span[2]/span[2]').text 
            prices.append(article_price)

        print(articles,prices)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
  unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='Report', report_name='mercadolibre_page_report'))
    