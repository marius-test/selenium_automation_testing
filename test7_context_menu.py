# delete unused imports
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
# driver = webdriver.Chrome(service=PATH)
# action_chains = ActionChains(driver)
# alert = Alert(driver)
title = "Context Menu"
text1 = "Context menu items are custom additions that appear in the right-click menu."
text2 = "Right-click in the box below to see one called 'the-internet'. When you click it, it will trigger a JavaScript alert."


class ContextMenu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Context Menu']").click()
    
    def test_title_text(self):
        driver = self.driver
        paragraph = driver.find_elements(by=By.TAG_NAME, value="p")
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h3").text, title)
        self.assertEqual(paragraph[0].text, text1)
        self.assertEqual(paragraph[1].text, text2)
        
    def test_properties(self):
        driver = self.driver
        driver.find_element(by=By.ID, value="hot-spot")
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
