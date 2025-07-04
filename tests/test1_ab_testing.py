import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/abtest"
expected_title = ["A/B Test Control", "A/B Test Variation 1"]
expected_text = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."


class TestABTesting(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(SECTION_HEADER_LOCATOR))
    
    def test_title_is_correct(self):
        actual_title = self.driver.find_element(By.TAG_NAME, "h3").text
        self.assertIn(actual_title, expected_title)  # usually expected then actual, but here actual is checked as member of a list
                         
    def test_text_is_correct(self):
        actual_text = self.driver.find_element(By.TAG_NAME, "p").text
        self.assertEqual(expected_text, actual_text)
    
    def tearDown(self):
        quit_driver(self.driver)
