import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class SanityTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\mariu\chromedriver.exe")
    
    def test(self):
        url = "https://the-internet.herokuapp.com/"
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
        title = driver.find_element(by=By.TAG_NAME, value="h1").text
        self.assertEqual(title, "Welcome to the-internet")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    