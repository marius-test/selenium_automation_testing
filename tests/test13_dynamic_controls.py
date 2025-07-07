import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com/dynamic_controls"


class TestDynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")
        wait_for_presence(self.driver, SECTION_HEADER_LOCATOR)
    
    def test_tick_checkbox(self):
        pass
    
    def test_untick_checkbox(self):
        pass
    
    def test_remove_ticked_checkbox(self):
        pass
    
    def test_add_ticked_checkbox(self):
        pass
    
    def test_enable_empty_field(self):
        pass
    
    def test_disable_empty_field(self):
        pass
    
    def test_disable_full_field(self):
        pass
    
    def test_enable_full_field(self):
        pass
    
    def tearDown(self):
        quit_driver(self.driver)
