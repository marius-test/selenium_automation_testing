import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# test data
expected_title = "Challenging DOM"
expected_text = "The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."
expected_button_list = ["foo", "bar", "baz", "qux"]
expected_header_list = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Diceret", "Action"]
expected_content_list0 = ["Iuvaret0", "Apeirian0", "Adipisci0", "Definiebas0", "Consequuntur0", "Phaedrum0"]
expected_content_list1 = ["Iuvaret1", "Apeirian1", "Adipisci1", "Definiebas1", "Consequuntur1", "Phaedrum1"]
expected_content_list2 = ["Iuvaret2", "Apeirian2", "Adipisci2", "Definiebas2", "Consequuntur2", "Phaedrum2"]
expected_content_list3 = ["Iuvaret3", "Apeirian3", "Adipisci3", "Definiebas3", "Consequuntur3", "Phaedrum3"]
expected_content_list4 = ["Iuvaret4", "Apeirian4", "Adipisci4", "Definiebas4", "Consequuntur4", "Phaedrum4"]
expected_content_list5 = ["Iuvaret5", "Apeirian5", "Adipisci5", "Definiebas5", "Consequuntur5", "Phaedrum5"]
expected_content_list6 = ["Iuvaret6", "Apeirian6", "Adipisci6", "Definiebas6", "Consequuntur6", "Phaedrum6"]
expected_content_list7 = ["Iuvaret7", "Apeirian7", "Adipisci7", "Definiebas7", "Consequuntur7", "Phaedrum7"]
expected_content_list8 = ["Iuvaret8", "Apeirian8", "Adipisci8", "Definiebas8", "Consequuntur8", "Phaedrum8"]
expected_content_list9 = ["Iuvaret9", "Apeirian9", "Adipisci9", "Definiebas9", "Consequuntur9", "Phaedrum9"]
expected_canvas_size = {'height': 202, 'width': 601}


class ChallengingDOM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Challenging DOM']").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3"))) 

    def test_title_text(self):
        self.assertEqual(expected_title, self.driver.find_element(By.TAG_NAME, "h3").text)
        self.assertEqual(expected_text, self.driver.find_element(By.TAG_NAME, "p").text)

    def test_side_buttons(self):
        tag_a_elements = self.driver.find_elements(By.TAG_NAME, "a")
        for x in range(1, 4):
            self.assertIn(expected_button_list, tag_a_elements[x].text)
        # self.assertIn(expected_button_list, driver.find_element(By.CLASS_NAME, "button").text)
        # self.assertIn(expected_button_list, driver.find_element(By.CLASS_NAME, "button alert").text)

    def test_table_actions(self):
        for x in range(1, 11):
            edit_buttons = self.driver.find_element(By.XPATH, f"//tbody/tr[{x}]/td[7]/a[1]")
            delete_buttons = self.driver.find_element(By.XPATH, f"//tbody/tr[{x}]/td[7]/a[2]")
            self.assertEqual("edit", edit_buttons.text)
            self.assertEqual("delete", delete_buttons.text)

    def test_table_columns(self):
        table_headers = self.driver.find_elements(By.TAG_NAME, "th")
        for x in range(0, 7):
            self.assertEqual(expected_header_list[x], table_headers[x].text)

    def test_table_content(self):
        table_content = self.driver.find_elements(By.TAG_NAME, "td")
        y = 0
        for x in range(0, 6):
            self.assertEqual(expected_content_list0[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(7, 13):
            self.assertEqual(expected_content_list1[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(14, 20):
            self.assertEqual(expected_content_list2[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(21, 27):
            self.assertEqual(expected_content_list3[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(28, 34):
            self.assertEqual(expected_content_list4[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(35, 41):
            self.assertEqual(expected_content_list5[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(42, 48):
            self.assertEqual(expected_content_list6[y], table_content[x].text)  
            y += 1
        y = 0
        for x in range(49, 55):
            self.assertEqual(expected_content_list7[y], table_content[x].text) 
            y += 1
        y = 0      
        for x in range(56, 62):
            self.assertEqual(expected_content_list8[y], table_content[x].text)
            y += 1
        y = 0
        for x in range(63, 69):
            self.assertEqual(expected_content_list9[y], table_content[x].text)
            y += 1

    def test_canvas_element(self):
        canvas = self.driver.find_element(By.ID, "canvas")
        self.assertDictEqual(expected_canvas_size, canvas.size)
        # to be added
        # save the canvas as .png, use OCR to verify that the word "Answer:" is displayed
        
    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()
