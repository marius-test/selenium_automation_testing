import time
import unittest
import urllib3
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pynput.keyboard import Key, Controller

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
driver.quit()

content_list = ["Iuvaret0", "Apeirian0", "Adipisci0", "Definiebas0", "Consequuntur0", "Phaedrum0"]

class ChallengingDOM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Challenging DOM']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        
    def test_table_content(self):
        driver = self.driver
        table_content = driver.find_elements(by=By.TAG_NAME, value="td")
        for x in range(0, 6):
            self.assertEqual(table_content[x].text, content_list[x])
                    
    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()
