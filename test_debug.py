import time
import unittest
import urllib3
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pynput.keyboard import Key, Controller

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
driver.quit()
