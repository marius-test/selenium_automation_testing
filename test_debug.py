import unittest
import urllib3
import requests
import pyautogui
import seletools
import time
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)
url = "https://the-internet.herokuapp.com/"


def test_debug():
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[12]/a").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[2]/a").click()
    time.sleep(120)


if __name__ == '__main__':
    test_debug()
