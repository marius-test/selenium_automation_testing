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
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        self.assertEqual(expected_title, self.driver.find_element(SECTION_HEADER_LOCATOR).text)

    def test_login_failed(self):
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        NOT_AUTHORIZED_LOCATOR = (By.TAG_NAME, "body")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        self.assertEqual("Not authorized", self.driver.file_detector(NOT_AUTHORIZED_LOCATOR).text)

    def tearDown(self):
        quit_driver(self.driver)
