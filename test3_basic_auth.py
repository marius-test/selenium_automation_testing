import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

PATH = Service("C:\\Users\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
username = password = "admin"
title = "Basic Auth"
text = "Congratulations! You must have the proper credentials."


class BasicAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.maximize_window()
        driver.get(url)
    """
    def test_login_successful(self):
        driver = self.driver
        login_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        driver.get(login_url)
        self.assertEqual(title, driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(text, driver.find_element(by=By.TAG_NAME, value="p").text)
    """
    def test_login_failed(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/basic_auth']").click()
        driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.ESCAPE)
        # self.assertEqual(driver.find_element(by=By.TAG_NAME, value="body").text, "Not authorized")

    def tearDown(self):
        time.sleep(60)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
