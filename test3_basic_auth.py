import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# test data
username = password = "admin"
expected_title = "Basic Auth"
expected_text = "Congratulations! You must have the proper credentials."


class BasicAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()

    def test_login_successful(self):
        login_url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(login_url)
        self.assertEqual(expected_title, self.driver.find_element(By.TAG_NAME, "h3").text)
        self.assertEqual(expected_text, self.driver.find_element(By.TAG_NAME, "p").text)

    def test_login_failed(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/basic_auth']").click()
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        time.sleep(2)
        self.assertEqual("Not authorized", self.driver.find_element(By.TAG_NAME, "body").text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
