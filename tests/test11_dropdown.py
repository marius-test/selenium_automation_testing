import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/"
expected_unselectable_text = "Please select an option"


class TestDropdown(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[11]/a").click()
   
    def test_unselectable(self):
        self.driver.find_element(By.ID, "dropdown").click()
        options = self.driver.find_elements(By.TAG_NAME, "option")
        self.assertAlmostEqual(expected_unselectable_text, options[0].text)
     
    def test_select_option1(self):
        self.driver.find_element(By.ID, "dropdown").click()
        options = self.driver.find_elements(By.TAG_NAME, "option")
        options[1].click()
        selected = options[1].get_attribute("selected")
        self.assertEqual("true", selected)

    def test_select_option2(self):
        self.driver.find_element(By.ID, "dropdown").click()
        options = self.driver.find_elements(By.TAG_NAME, "option")
        options[2].click()
        selected = options[2].get_attribute("selected")
        self.assertEqual("true", selected)
        
    def tearDown(self):
        quit_driver(self.driver)
