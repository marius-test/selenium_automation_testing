import unittest
import urllib3
import requests
import pyautogui
import time
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

# test data
expected_title = 'Dynamic Content'
expected_static_text_1 = "Accusantium eius ut architecto neque vel voluptatem vel nam eos minus ullam dolores voluptates enim sed voluptatem rerum qui sapiente nesciunt aspernatur et accusamus laboriosam culpa tenetur hic aut placeat error autem qui sunt."
expected_static_text_2 = "Omnis fugiat porro vero quas tempora quis eveniet ab officia cupiditate culpa repellat debitis itaque possimus odit dolorum et iste quibusdam quis dicta autem sint vel quo vel consequuntur dolorem nihil neque sunt aperiam blanditiis."
expected_static_image_1 = "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-5.jpg"
expected_static_image_2 = "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-6.jpg"
images_numbers = [0, 1, 2, 3, 4, 5, 6, 7]
expected_dynamic_images = [f"https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-{number}.jpg" for number in images_numbers]


class TestDynamicContent(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[12]/a").click()
        
    def test_title_is_correct(self):
        self.assertEqual(expected_title, self.driver.find_element(By.CSS_SELECTOR, "h3").text)
        self.driver.refresh()  # refreshing the page to test the dynamic/static content
        self.assertEqual(expected_title, self.driver.find_element(By.CSS_SELECTOR, "h3").text)

    def test_static_text(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[2]/a").click()
        self.assertEqual(expected_static_text_1, self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]').text)
        self.assertEqual(expected_static_text_2, self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]').text)
        self.driver.refresh()
        self.assertEqual(expected_static_text_1, self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]').text)
        self.assertEqual(expected_static_text_2, self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]').text)

    def test_static_images(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[2]/a").click()
        image_1 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/img')
        image_2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/img')
        image_1_src = image_1.get_attribute('src')
        image_2_src = image_2.get_attribute('src')
        self.assertEqual(expected_static_image_1, image_1_src)
        self.assertEqual(expected_static_image_2, image_2_src)
        self.driver.refresh()
        self.assertEqual(expected_static_image_1, image_1_src)
        self.assertEqual(expected_static_image_2, image_2_src)
 
    def test_dynamic_text(self):
        self.assertIsInstance(self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]').text, str)
        self.assertIsInstance(self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]').text, str)
        self.assertIsInstance(self.driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[2]').text, str)

    def test_dynamic_images(self):
        images = self.driver.find_elements(By.TAG_NAME, "img")
        for image in images:
            with self.subTest(image=image):
                self.assertEqual(image.tag_name, "img")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
