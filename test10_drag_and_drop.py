import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"


class DragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[10]/a").click()
    
    def test_drag_A_on_B(self):
        source_A = self.driver.find_element(By.ID, 'column-a')
        target_B = self.driver.find_element(By.ID, 'column-b')
        drag_and_drop(self.driver, source_A, target_B)
        header = self.driver.find_elements(By.TAG_NAME, "header")
        self.assertEqual("B", header[0].text)
        self.assertEqual("A", header[1].text)
         
    def test_drag_B_on_A(self):
        source_B = self.driver.find_element(By.ID, 'column-b')
        target_A = self.driver.find_element(By.ID, 'column-a')
        drag_and_drop(self.driver, source_B, target_A)
        header = self.driver.find_elements(By.TAG_NAME, "header")
        self.assertEqual("B", header[0].text)
        self.assertEqual("A", header[1].text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
