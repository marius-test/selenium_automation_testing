import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"


class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
    
    def test_image_displayed(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/broken_images']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(driver.find_element(by=By.TAG_NAME, value="h3")))
        
    def test_image_broken(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/broken_images']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(driver.find_element(by=By.TAG_NAME, value="h3")))
    
    def tearDown(self):
        self.driver.quit()


if __name__ == 'main':
    unittest.main()
