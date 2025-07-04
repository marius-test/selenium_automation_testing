import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/"
expected_title = "Welcome to the-internet"
expected_subtitle = "Available Examples"


class TestSmoke(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    
    def test_homepage_reached(self):
        self.assertEqual(expected_title, self.driver.find_element(By.TAG_NAME, "h1").text)
        self.assertEqual(expected_subtitle, self.driver.find_element(By.TAG_NAME, "h2").text)
    
    def tearDown(self):
        quit_driver(self.driver)
