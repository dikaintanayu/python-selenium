import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class ShopeeTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.addCleanup(self.driver.quit)

    def test_page_title(self):
        self.driver.get('https://shopee.com')
        self.assertIn('Leading Online Shopping Platform In Southeast Asia & Taiwan | Shopee', self.driver.title)

    def test_shopee_indonesia_page_title(self):
        self.driver.get('https://shopee.com')
        self.driver.find_element(By.XPATH, '//*[text()="Indonesia"]').click()
        sleep(2)
        self.assertIn('Shopee Indonesia | Situs Belanja Online Terlengkap & Terpercaya', self.driver.title)

    def test_shopee_Vietnam_page_title(self):
        self.driver.get('https://shopee.com')
        self.driver.find_element(By.XPATH,'//*[text()="Vietnam"]').click()
        sleep(2)
        self.assertIn('Shopee Việt Nam | Mua và Bán Trên Ứng Dụng Di Động Hoặc Website', self.driver.title)

    def test_search(self):
        self.driver.get('https://shopee.co.id')
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '[aria-controls="shopee-searchbar-listbox"]').send_keys('ASUS' + Keys.RETURN)
        sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)