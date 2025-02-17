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

# Test data
title = "Welcome to the-internet"
subtitle = "Available Examples"


class Smoke(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url)
        self.driver.maximize_window()
    
    def test_homepage_reached(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, title)
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h2").text, subtitle)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
