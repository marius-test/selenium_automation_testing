import unittest
import requests

import pyautogui
from pynput.keyboard import Key, Controller

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver

# TEST DATA
URL = "https://the-internet.herokuapp.com/digest_auth"
USERNAME = PASSWORD = "admin"
LOGIN_URL = f"https://{USERNAME}:{PASSWORD}@the-internet.herokuapp.com/digest_auth"
expected_title = "Digest Auth"
expected_message = "Congratulations! You must have the proper credentials."
expected_response = "<Response [401]>"


class TestDigestAuth(unittest.TestCase):
    SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
    MESSAGE_PARAGRAPH_LOCATOR = (By.TAG_NAME, "p")
    
    def setUp(self):
        self.driver = get_driver()

    def test_login_url_successful(self):

        self.driver.get(LOGIN_URL)
        self.assertEqual(expected_title, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)
        self.assertEqual(expected_message, self.driver.find_element(*self.MESSAGE_PARAGRAPH_LOCATOR).text)

    def test_login_credentials_successful(self):
        self.driver.get(URL)
        pyautogui.write(USERNAME)
        pyautogui.press('tab')
        pyautogui.write(PASSWORD)
        pyautogui.press('enter')
        self.assertEqual(expected_title, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)
        self.assertEqual(expected_message, self.driver.find_element(*self.MESSAGE_PARAGRAPH_LOCATOR).text)

    def test_login_failed(self):
        self.driver.get(URL)
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        response = requests.get(self.driver.current_url, stream=True)
        self.assertEqual(expected_response, str(response))

    def tearDown(self):
        quit_driver(self.driver)
