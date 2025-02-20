import unittest
import requests
import pyautogui
from pynput.keyboard import Key, Controller
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
username = password = "admin"
expected_title = "Digest Auth"
expected_text = "Congratulations! You must have the proper credentials."
expected_response = "<Response [401]>"


class TestDigestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    def test_login_url_successful(self):
        login_url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
        self.driver.get(login_url)
        self.assertEqual(expected_title, self.driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(expected_text, self.driver.find_element(by=By.TAG_NAME, value="p").text)

    def test_login_credentials_successful(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[8]/a").click()
        pyautogui.write(username)
        pyautogui.press('tab')
        pyautogui.write(password)
        pyautogui.press('enter')
        self.assertEqual(expected_title, self.driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(expected_text, self.driver.find_element(by=By.TAG_NAME, value="p").text)

    def test_login_failed(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[8]/a").click()
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        response = requests.get(self.driver.current_url, stream=True)
        self.assertEqual(expected_response, str(response))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
