import unittest

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com"
expected_title = "Welcome to the-internet"
expected_subtitle = "Available Examples"


class TestSmoke(unittest.TestCase):
    HEADER_LOCATOR = (By.TAG_NAME, "h1")
    
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        wait_for_presence(self.driver, self.HEADER_LOCATOR)
        
    def test_homepage_reached(self):
        actual_title = self.driver.find_element(*self.HEADER_LOCATOR).text
        actual_subtitle = self.driver.find_element(By.TAG_NAME, "h2").text
        self.assertEqual(expected_title, actual_title)
        self.assertEqual(expected_subtitle, actual_subtitle)
    
    def tearDown(self):
        quit_driver(self.driver)
