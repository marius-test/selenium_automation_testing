import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pynput.keyboard import Key, Controller

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/basic_auth"
username = password = "admin"
expected_title = "Basic Auth"
expected_text = "Congratulations! You must have the proper credentials."


class TestBasicAuth(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)

    def test_login_successful(self):
        login_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(login_url)
        self.assertEqual(expected_title, self.driver.find_element(By.TAG_NAME, "h3").text)
        self.assertEqual(expected_text, self.driver.find_element(By.TAG_NAME, "p").text)

    def test_login_failed(self):
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        time.sleep(2)
        self.assertEqual("Not authorized", self.driver.find_element(By.TAG_NAME, "body").text)

    def tearDown(self):
        quit_driver(self.driver)
