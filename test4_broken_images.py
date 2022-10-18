import time
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"


class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
    
    def test_broken_images(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/broken_images']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        image_list = driver.find_elements(by=By.TAG_NAME, value="img")
        broken_images = 0
        for image in image_list:
            response = requests.get(image.get_attribute('src'), stream=True)
            if response.status_code != 200:
                broken_images += 1
        self.assertEqual(str(broken_images), "0")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
