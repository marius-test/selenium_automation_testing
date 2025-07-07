import unittest

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com/dropdown"
expected_placeholder_text = "Please select an option"


class TestDropdown(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        wait_for_presence(self.driver, SECTION_HEADER_LOCATOR)
   
    def test_placeholder(self):
        self.driver.find_element(By.ID, "dropdown").click()
        actual_placeholder_text = self.driver.find_elements(By.TAG_NAME, "option")
        self.assertAlmostEqual(expected_placeholder_text, actual_placeholder_text[0].text)
     
    def test_select_options(self):
        self.driver.find_element(By.ID, "dropdown").click()
        options = self.driver.find_elements(By.TAG_NAME, "option")

        for i in range(1, len(options)):
            options[i].click()
            selected = options[i].get_attribute("selected")
            self.assertEqual("true", selected, f"Option {i} was not selected.")
        
    def tearDown(self):
        quit_driver(self.driver)
