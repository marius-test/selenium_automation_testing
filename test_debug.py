# import unittest
# import urllib3
# import requests
# import pyautogui
# import seletools
import time
import unittest
# from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from webdriver_manager.chrome import ChromeDriverManager



PATH = Service("C:\\Users\\marius\\chromedriver.exe")
# chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=PATH)
url = "https://the-internet.herokuapp.com/"


def test_debug():
    driver.get(url)
    driver.maximize_window()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[12]/a").click()
    """
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p[2]/a").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    image_1 = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/img')
    image_2 = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/img')
    image_1_src = image_1.get_attribute('src')
    image_2_src = image_2.get_attribute('src')
    print(image_1_src)
    print(image_2_src)
    """
    dynamic_text = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]').text
    print(dynamic_text)
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    test_debug()
