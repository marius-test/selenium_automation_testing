import unittest
from time import sleep

import urllib3
import requests
import pyautogui
from pynput.keyboard import Key, Controller

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.driver_factory import get_driver, quit_driver
from seletools.actions import drag_and_drop

# test data
url = "https://the-internet.herokuapp.com"


class TestName(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        # initialize ActionChains and Alert here if needed
        # self.action_chains = ActionChains(self.driver)
        # self.alert = Alert(self.driver)
    
    def test_x(self):
        # locators, waits, actions
        self.assertEqual(1, 1)
    
    def test_y(self):
        # locators, waits, actions
        self.assertEqual(True, False)
    
    def tearDown(self):
        quit_driver(self.driver)
