import unittest
import requests

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com/disappearing_elements"
expected_header = "Disappearing Elements"
expected_paragraph = "This example demonstrates when elements on a page change by disappearing/reappearing on each page load."
expected_buttons = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
expected_footer = "Powered by Elemental Selenium"
expected_link = "http://elementalselenium.com/"
expected_path = ["", "about/", "contact-us/", "portfolio/", "gallery/"]
expected_response = ["<Response [200]>", "<Response [404]>", "<Response [404]>", "<Response [404]>"]


class TestDisappearingElements(unittest.TestCase):
    SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")

    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        wait_for_presence(self.driver, self.SECTION_HEADER_LOCATOR)

    def test_header_and_paragraph(self):
        self.assertEqual(expected_header, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)
        self.assertEqual(expected_paragraph, self.driver.find_element(By.TAG_NAME, "p").text)
    
    def test_buttons_text(self):
        list_of_buttons = self.driver.find_elements(By.TAG_NAME, "li")
        for i, button in enumerate(list_of_buttons):
            self.assertEqual(expected_buttons[i], button.text)

    def test_buttons_redirect(self):
        list_of_buttons = self.driver.find_elements(By.TAG_NAME, "a")
        for i in range(0, 4):
            self.assertEqual(f"https://the-internet.herokuapp.com/{expected_path[i]}", list_of_buttons[i + 1].get_attribute("href"))
            list_of_buttons[i + 1].click()
            response = requests.get(self.driver.current_url, stream=True)
            self.assertEqual(expected_response[i], str(response))
            self.driver.back()
      
    def test_missing_button(self):
        try:
            wait_for_presence(self.driver, (By.CSS_SELECTOR, "#content > div > ul > li:nth-child(5) > a"), timeout=2)
        except TimeoutException:
            button_is_displayed = 'No'
        else:
            button_is_displayed = 'Yes'
        finally:
            print(f"The button is displayed: {button_is_displayed}")
            self.assertIn(button_is_displayed, ['Yes', 'No'])

    def test_footer(self):
        actual_footer = self.driver.find_element(By.CSS_SELECTOR, "#page-footer > div > div")
        actual_link = self.driver.find_element(By.CSS_SELECTOR, "#page-footer > div > div > a")
        self.assertEqual(expected_footer, actual_footer.text)
        self.assertEqual(expected_link, actual_link.get_attribute("href"))

    def tearDown(self):
        quit_driver(self.driver)
