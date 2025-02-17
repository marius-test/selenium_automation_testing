import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# PATH = Service("C:\\Users\\marius\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# Test data
expected_unselectable_text = "Please select an option"


class Dropdown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
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
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
