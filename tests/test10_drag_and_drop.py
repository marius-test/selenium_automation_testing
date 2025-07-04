import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver
from seletools.actions import drag_and_drop

# test data
url = "https://the-internet.herokuapp.com/"


class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
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
        quit_driver(self.driver)
