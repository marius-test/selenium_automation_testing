import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

PATH = Service("C:\\Users\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
# test data here


class TestName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
    
    def test_x(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def test_y(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
