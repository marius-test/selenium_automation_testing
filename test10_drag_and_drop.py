import unittest
import urllib3
import requests
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"


class DragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[10]/a").click()
    
    def test_drag_A_on_B(self):
        driver = self.driver
        action = ActionChains(driver)
        column_a = driver.find_element(by=By.XPATH, value='//*[@id="column-a"]')
        column_b = driver.find_element(by=By.XPATH, value='//*[@id="column-b"]')
    
    def test_drag_B_on_A(self):
        driver = self.driver
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
