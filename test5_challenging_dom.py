import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
title = "Challenging DOM"
text = "The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."
button_list = ["foo", "bar", "baz", "qux"]
header_list = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Diceret", "Action"]

class TestName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Challenging DOM']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3"))) 
    """
    def test_title_text(self):
        driver = self.driver
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h3").text, title)
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="p").text, text)

    def test_side_buttons(self):
        driver = self.driver
        tag_a_elements = driver.find_elements(by=By.TAG_NAME, value="a")
        for x in range(1, 4):
            self.assertIn(tag_a_elements[x].text, button_list)
        # self.assertIn(driver.find_element(by=By.CLASS_NAME, value="button").text, button_list)
        # self.assertIn(driver.find_element(by=By.CLASS_NAME, value="button alert").text, button_list)

    def test_table_actions(self):
        driver = self.driver
        for x in range(1, 11):
            edit_buttons = driver.find_element(by=By.XPATH, value=f"//tbody/tr[{x}]/td[7]/a[1]")
            delete_buttons = driver.find_element(by=By.XPATH, value=f"//tbody/tr[{x}]/td[7]/a[2]")
            self.assertEqual(edit_buttons.text, "edit")
            self.assertEqual(delete_buttons.text, "delete")

    def test_table_columns(self):
        driver = self.driver
        table_headers = driver.find_elements(by=By.TAG_NAME, value="th")
        for x in range(0, 7):
            self.assertEqual(table_headers[x].text, header_list[x])
    """
    def test_table_content(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    """
    def test_canvas_element(self):
        driver = self.driver
        # locators, waits, actions here
        self.assertEqual(1, 1)
    """
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
