import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"


class DragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[10]/a").click()
    
    def test_drag_A_on_B(self):
        driver = self.driver
        source_A = driver.find_element(by=By.ID, value='column-a')
        target_B = driver.find_element(by=By.ID, value='column-b')
        drag_and_drop(driver, source_A, target_B)
        header = driver.find_elements(by=By.TAG_NAME, value="header")
        self.assertEqual(header[0].text, "B")
        self.assertEqual(header[1].text, "A")
         
    def test_drag_B_on_A(self):
        driver = self.driver
        source_B = driver.find_element(by=By.ID, value='column-b')
        target_A = driver.find_element(by=By.ID, value='column-a')
        drag_and_drop(driver, source_B, target_A)
        header = driver.find_elements(by=By.TAG_NAME, value="header")
        self.assertEqual(header[0].text, "B")
        self.assertEqual(header[1].text, "A")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
