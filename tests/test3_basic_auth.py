import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pynput.keyboard import Key, Controller

from utils.driver_factory import get_driver, quit_driver

# TEST DATA
USERNAME = PASSWORD = "admin"
expected_title = "Basic Auth"
expected_unauthorized_message = "Not authorized"

class TestBasicAuth(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()

    def test_login_successful(self):
        login_url = f"https://{USERNAME}:{PASSWORD}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(login_url)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(SECTION_HEADER_LOCATOR))
        actual_title = self.driver.find_element(*SECTION_HEADER_LOCATOR).text
        self.assertEqual(expected_title, actual_title)


    def test_login_failed(self):
        URL = "https://the-internet.herokuapp.com/basic_auth"
        self.driver.get(URL)
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        BODY_TEXT_LOCATOR = (By.TAG_NAME, "body")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(BODY_TEXT_LOCATOR))
        unauthorized_message = self.driver.find_element(*BODY_TEXT_LOCATOR).text
        self.assertEqual(expected_unauthorized_message, unauthorized_message)


    def tearDown(self):
        quit_driver(self.driver)
