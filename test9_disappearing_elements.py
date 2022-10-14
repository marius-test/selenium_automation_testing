import time
import unittest
import urllib3
import requests
import pyautogui
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
header = "Disappearing Elements"
paragraph = "This example demonstrates when elements on a page change by disappearing/reappearing on each page load."
expected_buttons = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
expected_footer = "Powered by Elemental Selenium"
expected_footer_link = "http://elementalselenium.com/"


class DisappearingElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[9]/a").click()
    """
    def test_header_and_paragraph(self):
        driver = self.driver
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h3").text, header)
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="p").text, paragraph)
    
    def test_buttons_text(self):
        driver = self.driver
        list_of_buttons = driver.find_elements(by=By.TAG_NAME, value="li")
        i = 0
        for button in list_of_buttons:
            self.assertEqual(list_of_buttons[i].text, expected_buttons[i])
            i += 1
    """
    def test_buttons_redirect(self):
        driver = self.driver
        list_of_buttons = driver.find_elements(by=By.TAG_NAME, value="a")
        i = 0
        for buttons in list_of_buttons:
            print(list_of_buttons[i].get_attribute("href"))
            i += 1
        self.assertEqual(list_of_buttons[1].get_attribute("href"), "https://the-internet.herokuapp.com/")
        self.assertEqual(list_of_buttons[2].get_attribute("href"), "https://the-internet.herokuapp.com/about/")
        self.assertEqual(list_of_buttons[3].get_attribute("href"), "https://the-internet.herokuapp.com/contact-us/")
        self.assertEqual(list_of_buttons[4].get_attribute("href"), "https://the-internet.herokuapp.com/portfolio/")
        
        # if
        # self.assertEqual(list_of_buttons[5].get_attribute("href"), "https://the-internet.herokuapp.com/gallery/")

    """
    def test_footer(self):
        driver = self.driver
        footer = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div")
        link = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/a")
        self.assertEqual(footer.text, expected_footer)
        self.assertEqual(link.get_attribute("href"), expected_footer_link)
    """
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
