from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from seletools.actions import drag_and_drop


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("http://the-internet.herokuapp.com/drag_and_drop")
source_A = driver.find_element(By.ID, "column-a")
target_B = driver.find_element(By.ID, "column-b")
drag_and_drop(driver, source_A, target_B)
driver.quit()
