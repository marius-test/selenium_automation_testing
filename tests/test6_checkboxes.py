import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/"
expected_text = "checkbox 1\ncheckbox 2"


class TestCheckboxes(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Checkboxes']").click()

    def test_text(self):
        checkbox_string = self.driver.find_element(By.TAG_NAME, "form").text
        self.assertEqual(expected_text, checkbox_string)

    def test_check(self):
        checkbox = self.driver.find_elements(By.TAG_NAME, "input")
        if checkbox[0].is_selected() == False:
            checkbox[0].click()
        self.assertTrue(checkbox[0].is_selected())
        if checkbox[1].is_selected() == False:
            checkbox[1].click()
        self.assertTrue(checkbox[1].is_selected())

    def test_uncheck(self):
        checkbox = self.driver.find_elements(By.TAG_NAME, "input")
        if checkbox[0].is_selected() == True:
            checkbox[0].click()
        self.assertFalse(checkbox[0].is_selected())
        if checkbox[1].is_selected() == True:
            checkbox[1].click()
        self.assertFalse(checkbox[1].is_selected())

    def tearDown(self):
        quit_driver(self.driver)
