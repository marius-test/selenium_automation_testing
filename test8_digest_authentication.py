import unittest
import requests
import pyautogui
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
username = password = "admin"
title = "Digest Auth"
text = "Congratulations! You must have the proper credentials."
expected_response = "<Response [401]>"


class DigestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()

    def test_login_url_successful(self):
        driver = self.driver
        login_url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
        driver.get(login_url)
        self.assertEqual(title, driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(text, driver.find_element(by=By.TAG_NAME, value="p").text)

    def test_login_credentials_successful(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[8]/a").click()
        pyautogui.write(username)
        pyautogui.press('tab')
        pyautogui.write(password)
        pyautogui.press('enter')
        self.assertEqual(title, driver.find_element(by=By.TAG_NAME, value="h3").text)
        self.assertEqual(text, driver.find_element(by=By.TAG_NAME, value="p").text)

    def test_login_failed(self):
        driver = self.driver
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[8]/a").click()
        Controller().press(Key.esc)
        Controller().release(Key.esc)
        response = requests.get(driver.current_url, stream=True)
        self.assertEqual(str(response), expected_response)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
