import unittest

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence
from seletools.actions import drag_and_drop

# TEST DATA
URL = "https://the-internet.herokuapp.com/drag_and_drop"


class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        wait_for_presence(self.driver, SECTION_HEADER_LOCATOR)
    
    def test_drag_A_on_B(self):
        source_A = self.driver.find_element(By.ID, 'column-a')
        target_B = self.driver.find_element(By.ID, 'column-b')
        drag_and_drop(self.driver, source_A, target_B)
        header = self.driver.find_elements(By.TAG_NAME, "header")
        self.assertEqual("B", header[0].text)
        self.assertEqual("A", header[1].text)
         
    def test_drag_B_on_A(self):
        source_B = self.driver.find_element(By.ID, 'column-b')
        target_A = self.driver.find_element(By.ID, 'column-a')
        drag_and_drop(self.driver, source_B, target_A)
        header = self.driver.find_elements(By.TAG_NAME, "header")
        self.assertEqual("B", header[0].text)
        self.assertEqual("A", header[1].text)

    def tearDown(self):
        quit_driver(self.driver)
