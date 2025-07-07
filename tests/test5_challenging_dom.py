import unittest

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com/challenging_dom"
expected_title = "Challenging DOM"
expected_text = "The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."
expected_buttons = ["foo", "bar", "baz", "qux"]
expected_headers = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Diceret", "Action"]
expected_table_content = [
    [f"Iuvaret{i}", f"Apeirian{i}", f"Adipisci{i}", f"Definiebas{i}", f"Consequuntur{i}", f"Phaedrum{i}"] 
    for i in range(10)
    ]
expected_canvas_size = {'height': 202, 'width': 601}


class TestChallengingDOM(unittest.TestCase):
    SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")

    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        wait_for_presence(self.driver, self.SECTION_HEADER_LOCATOR)

    def test_title_text(self):
        self.assertEqual(expected_title, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)
        self.assertEqual(expected_text, self.driver.find_element(By.TAG_NAME, "p").text)

    def test_side_buttons(self):
        tag_a_elements = self.driver.find_elements(By.TAG_NAME, "a")
        for x in range(1, 4):
            self.assertIn(tag_a_elements[x].text, expected_buttons)  # usually expected then actual, but here actual is checked as member of a list

    def test_table_actions(self):
        for x in range(1, 11):
            edit_buttons = self.driver.find_element(By.CSS_SELECTOR, f"#content > div > div > div > div.large-10.columns > table > tbody > tr:nth-child({x}) > td:nth-child(7) > a:nth-child(1)")
            delete_buttons = self.driver.find_element(By.CSS_SELECTOR, f"#content > div > div > div > div.large-10.columns > table > tbody > tr:nth-child({x}) > td:nth-child(7) > a:nth-child(2)")
            self.assertEqual("edit", edit_buttons.text)
            self.assertEqual("delete", delete_buttons.text)

    def test_table_columns(self):
        table_headers = self.driver.find_elements(By.TAG_NAME, "th")
        for x in range(0, 7):
            self.assertEqual(expected_headers[x], table_headers[x].text)

    def test_table_content(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
        expected_rows = expected_table_content

        for row_index, expected_row in enumerate(expected_rows):
            cells = rows[row_index].find_elements(By.TAG_NAME, "td")
            # only check first 6 cells (skip last cell with action buttons)
            for col_index, expected_cell in enumerate(expected_row):
                actual_cell = cells[col_index].text
                self.assertEqual(expected_cell, actual_cell,f"Mismatch at row {row_index}, column {col_index}.")

    def test_canvas_element(self):
        canvas = self.driver.find_element(By.ID, "canvas")
        self.assertDictEqual(expected_canvas_size, canvas.size)
        
    def tearDown(self):
        quit_driver(self.driver)
