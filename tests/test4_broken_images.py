import unittest
import requests

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com/broken_images"


class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        wait_for_presence(self.driver, SECTION_HEADER_LOCATOR)
    
    def test_broken_images(self):
        IMAGE_LOCATOR = (By.TAG_NAME, "img")
        image_list = self.driver.find_elements(*IMAGE_LOCATOR)
        broken_images = 0
        for image in image_list:
            response = requests.get(image.get_attribute('src'), stream=True)
            if response.status_code != 200:
                broken_images += 1
        self.assertEqual("2", str(broken_images))
    
    def tearDown(self):
        quit_driver(self.driver)
