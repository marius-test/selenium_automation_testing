import unittest
import urllib3
import requests
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# Test data
expected_title = 'Dynamic Content'
expected_static_text_1 = "Accusantium eius ut architecto neque vel voluptatem vel nam eos minus ullam dolores voluptates enim sed voluptatem rerum qui sapiente nesciunt aspernatur et accusamus laboriosam culpa tenetur hic aut placeat error autem qui sunt."
expected_static_text_2 = "Omnis fugiat porro vero quas tempora quis eveniet ab officia cupiditate culpa repellat debitis itaque possimus odit dolorum et iste quibusdam quis dicta autem sint vel quo vel consequuntur dolorem nihil neque sunt aperiam blanditiis."
expected_static_image_1 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg"
expected_static_image_2 = "/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg"
expected_dynamic_images = ["/img/avatars/Original-Facebook-Geek-Profile-Avatar-1.jpg", "/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg", "/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg"]


class DynamicContent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[12]/a").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[2]/a").click()
        
    def test_title_is_correct(self):
        self.assertEqual(expected_title, self.driver.find_element(By.CSS_SELECTOR, "h3").text)
        self.driver.refresh()  # refreshing the page to test the dynamic/static content
        self.assertEqual(expected_title, self.driver.find_element(By.CSS_SELECTOR, "h3").text)

    def test_static_text(self):
        self.assertEqual(expected_static_text_1, self.driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div[2]/text()").text)
        
'''
    def test_static_images(self):
        pass
    
    def test_dynamic_text(self):
        pass
    
    def test_dynamic_images(self):
        pass
    
    def tearDown(self):
        self.driver.quit()
'''

if __name__ == '__main__':
    unittest.main()
