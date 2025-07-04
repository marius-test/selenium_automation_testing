import unittest
import requests

import pyautogui
from pynput.keyboard import Key, Controller

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/"
username = password = "admin"
expected_title = "Digest Auth"
expected_text = "Congratulations! You must have the proper credentials."
expected_response = "<Response [401]>"


class TestDigestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
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
        quit_driver(self.driver)
