import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
s = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

title = "Challenging DOM"
text = "The hardest part in automated web testing is finding the best locators (e.g., ones that well named, unique, and unlikely to change). It's more often than not that the application you're testing was not built with this concept in mind. This example demonstrates that with unique IDs, a table with no helpful locators, and a canvas element."
button_list = ["foo", "bar", "baz", "qux"]
header_list = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet", "Diceret", "Action"]
content_list0 = ["Iuvaret0", "Apeirian0", "Adipisci0", "Definiebas0", "Consequuntur0", "Phaedrum0"]
content_list1 = ["Iuvaret1", "Apeirian1", "Adipisci1", "Definiebas1", "Consequuntur1", "Phaedrum1"]
content_list2 = ["Iuvaret2", "Apeirian2", "Adipisci2", "Definiebas2", "Consequuntur2", "Phaedrum2"]
content_list3 = ["Iuvaret3", "Apeirian3", "Adipisci3", "Definiebas3", "Consequuntur3", "Phaedrum3"]
content_list4 = ["Iuvaret4", "Apeirian4", "Adipisci4", "Definiebas4", "Consequuntur4", "Phaedrum4"]
content_list5 = ["Iuvaret5", "Apeirian5", "Adipisci5", "Definiebas5", "Consequuntur5", "Phaedrum5"]
content_list6 = ["Iuvaret6", "Apeirian6", "Adipisci6", "Definiebas6", "Consequuntur6", "Phaedrum6"]
content_list7 = ["Iuvaret7", "Apeirian7", "Adipisci7", "Definiebas7", "Consequuntur7", "Phaedrum7"]
content_list8 = ["Iuvaret8", "Apeirian8", "Adipisci8", "Definiebas8", "Consequuntur8", "Phaedrum8"]
content_list9 = ["Iuvaret9", "Apeirian9", "Adipisci9", "Definiebas9", "Consequuntur9", "Phaedrum9"]
canvas_size = {'height': 202, 'width': 601}


class ChallengingDOM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Challenging DOM']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3"))) 

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

    def test_table_content(self):
        driver = self.driver
        table_content = driver.find_elements(by=By.TAG_NAME, value="td")
        y = 0
        for x in range(0, 6):
            self.assertEqual(table_content[x].text, content_list0[y])
            y += 1
        y = 0
        for x in range(7, 13):
            self.assertEqual(table_content[x].text, content_list1[y])
            y += 1
        y = 0
        for x in range(14, 20):
            self.assertEqual(table_content[x].text, content_list2[y])
            y += 1
        y = 0
        for x in range(21, 27):
            self.assertEqual(table_content[x].text, content_list3[y])
            y += 1
        y = 0
        for x in range(28, 34):
            self.assertEqual(table_content[x].text, content_list4[y])
            y += 1
        y = 0
        for x in range(35, 41):
            self.assertEqual(table_content[x].text, content_list5[y])
            y += 1
        y = 0
        for x in range(42, 48):
            self.assertEqual(table_content[x].text, content_list6[y])  
            y += 1
        y = 0
        for x in range(49, 55):
            self.assertEqual(table_content[x].text, content_list7[y]) 
            y += 1
        y = 0      
        for x in range(56, 62):
            self.assertEqual(table_content[x].text, content_list8[y])
            y += 1
        y = 0
        for x in range(63, 69):
            self.assertEqual(table_content[x].text, content_list9[y])
            y += 1

    def test_canvas_element(self):
        driver = self.driver
        canvas = driver.find_element(by=By.ID, value="canvas")
        self.assertDictEqual(canvas.size , canvas_size)
        # to be added
        # save the canvas as .png, use OCR to verify that the word "Answer:" is displayed
        
    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()
