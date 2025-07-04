import unittest
import urllib3
import requests
import pyautogui
from time import sleep

from pynput.keyboard import Key, Controller

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/"

class TestDynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[13]/a').click()
    
    def test_tick_checkbox(self):
        pass
    
    def test_untick_checkbox(self):
        pass
    
    def test_remove_ticked_checkbox(self):
        pass
    
    def test_add_ticked_checkbox(self):
        pass
    
    def test_enable_empty_field(self):
        pass
    
    def test_disable_empty_field(self):
        pass
    
    def test_disable_full_field(self):
        pass
    
    def test_enable_full_field(self):
        pass
    
    def tearDown(self):
        quit_driver(self.driver)
