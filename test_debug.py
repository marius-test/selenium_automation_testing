import time
import unittest
import urllib3
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pynput.keyboard import Key, Controller

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"

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


class ChallengingDOM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Challenging DOM']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        
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

    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()
