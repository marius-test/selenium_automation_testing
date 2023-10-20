import unittest
import urllib3
import requests
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
s = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# action_chains = ActionChains(driver)
# alert = Alert(driver)

expected_title = 'Dynamic Content'


class TestName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    
    def test_x(self):
        driver = self.driver
        self.assertEqual(1, 1)
    
    def test_y(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
