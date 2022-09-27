import time
import unittest
import urllib3
import requests
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
# driver = webdriver.Chrome(Service=PATH)
# action_chains = ActionChains(driver)
# alert = Alert(driver)


class Checkboxes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Checkboxes']").click()
        
    def test1(self):
        self.assertEqual(1, 1)
    
    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()
