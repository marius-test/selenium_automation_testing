import unittest

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence, safe_wait

# TEST DATA
URL = "https://the-internet.herokuapp.com/context_menu"
expected_title = "Context Menu"
expected_paragraph_1 = "Context menu items are custom additions that appear in the right-click menu."
expected_paragraph_2 = "Right-click in the box below to see one called 'the-internet'. When you click it, it will trigger a JavaScript alert."
expected_alert = "You selected a context menu"


class TestContextMenu(unittest.TestCase):
    SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")

    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        wait_for_presence(self.driver, self.SECTION_HEADER_LOCATOR)

    def test_title_text(self):
        actual_paragraph = self.driver.find_elements(By.TAG_NAME, "p")
        self.assertEqual(expected_title, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)
        self.assertEqual(expected_paragraph_1, actual_paragraph[0].text)
        self.assertEqual(expected_paragraph_2, actual_paragraph[1].text)
        
    def test_box_properties(self):
        style = self.driver.find_element(By.ID, "hot-spot").get_attribute("style")
        self.assertEqual("border-style: dashed; border-width: 5px; width: 250px; height: 150px;", style)

    def test_alert_box_open(self):
        actual_alert = Alert(self.driver)
        action = ActionChains(self.driver)
        box = self.driver.find_element(By.ID, "hot-spot")
        action.context_click(box).perform()
        self.assertEqual(expected_alert, actual_alert.text)

    def test_alert_box_closed(self):
        action = ActionChains(self.driver)
        box = self.driver.find_element(By.ID, "hot-spot")
        action.context_click(box).perform()

        actual_alert = Alert(self.driver)
        self.assertEqual(expected_alert, actual_alert.text)
        actual_alert.accept()

        alert = safe_wait(self.driver, EC.alert_is_present(), timeout=2)
        alert_is_present = 'Yes' if alert else 'No'

        self.assertTrue(alert_is_present == 'No')

    def tearDown(self):
        quit_driver(self.driver)
