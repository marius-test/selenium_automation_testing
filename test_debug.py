import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pynput.keyboard import Key, Controller
import time

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
url = "https://the-internet.herokuapp.com/"
driver.get(url)
driver.maximize_window()
driver.find_element(by=By.CSS_SELECTOR, value="a[href='/basic_auth']").click()
Controller().press(Key.esc)
Controller().release(Key.esc)
time.sleep(2)
print(driver.find_element(by=By.XPATH, value="//body").text)
