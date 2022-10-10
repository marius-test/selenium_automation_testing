import time
import unittest
import requests
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
username = password = "admin"
title = "Digest Auth"
text = "Congratulations! You must have the proper credentials."


class DigestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
    
    def test_login_url_successful(self):
        driver = self.driver
        login_url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
        driver.get(login_url)
        self.assertEqual(title, driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(text, driver.find_element(by=By.TAG_NAME, value="p").text)
    """     
    def test_login_credentials_successful(self):
        driver = self.driver
        action_chains = ActionChains(driver)
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[8]/a").click()
        action_chains.send_keys(username)
        Controller.press(Key.tab)
        Controller().release(Key.tab)
        action_chains.send_keys(password)
        Controller().press(Key.enter)
        Controller().release(Key.enter)
        self.assertEqual(title, driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(text, driver.find_element(by=By.TAG_NAME, value="p").text)
    """  
    def test_login_failed(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[8]/a").click()
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        response = requests.get(driver.current_url, stream=True)
        self.assertEqual(str(response), "<Response [401]>")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
