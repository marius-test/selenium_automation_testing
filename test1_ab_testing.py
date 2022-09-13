import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
title = "A/B Test Control"
text = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."
url = "https://the-internet.herokuapp.com/"


class ABTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
    
    def test_title_is_correct(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/abtest']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h3").text, title)
                         
    def test_text_is_correct(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/abtest']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="p").text, text)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
