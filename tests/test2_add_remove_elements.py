import unittest

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence, wait_for_invisibility

# TEST DATA
URL = "https://the-internet.herokuapp.com/add_remove_elements/"


class TestAddRemoveElement(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        wait_for_presence(self.driver, SECTION_HEADER_LOCATOR)
        
    def test_add_element(self):
        add_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
        add_button.click()
        delete_button = self.driver.find_element(By.CSS_SELECTOR, ".added-manually")
        self.assertEqual("Delete", delete_button.text)

    def test_remove_element(self):
        add_button = self.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
        add_button.click()
        delete_button = self.driver.find_element(By.CSS_SELECTOR, ".added-manually")     
        delete_button.click()
        self.assertTrue(wait_for_invisibility(self.driver, (By.CSS_SELECTOR, ".added-manually")))

    def tearDown(self):
        quit_driver(self.driver)
