import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
s = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

expected_unselectable_text = "Please select an option"


class TestDropdown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[11]/a").click()
   
    def test_unselectable(self):
        driver = self.driver
        driver.find_element(by=By.ID, value="dropdown").click()
        options = driver.find_elements(by=By.TAG_NAME, value="option")
        self.assertAlmostEqual(options[0].text, expected_unselectable_text)
     
    def test_select_option1(self):
        driver = self.driver
        driver.find_element(by=By.ID, value="dropdown").click()
        options = driver.find_elements(by=By.TAG_NAME, value="option")
        options[1].click()
        selected = options[1].get_attribute("selected")
        self.assertEqual(selected, "true")

    def test_select_option2(self):
        driver = self.driver
        driver.find_element(by=By.ID, value="dropdown").click()
        options = driver.find_elements(by=By.TAG_NAME, value="option")
        options[2].click()
        selected = options[2].get_attribute("selected")
        self.assertEqual(selected, "true")
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
