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
expected_text = "checkbox 1\ncheckbox 2"


class Checkboxes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Checkboxes']").click()

    def test_text(self):
        checkbox_string = self.driver.find_element(By.TAG_NAME, "form").text
        self.assertEqual(expected_text, checkbox_string)

    def test_check(self):
        checkbox = self.driver.find_elements(By.TAG_NAME, "input")
        if checkbox[0].is_selected() == False:
            checkbox[0].click()
        self.assertTrue(checkbox[0].is_selected())
        if checkbox[1].is_selected() == False:
            checkbox[1].click()
        self.assertTrue(checkbox[1].is_selected())

    def test_uncheck(self):
        checkbox = self.driver.find_elements(By.TAG_NAME, "input")
        if checkbox[0].is_selected() == True:
            checkbox[0].click()
        self.assertFalse(checkbox[0].is_selected())
        if checkbox[1].is_selected() == True:
            checkbox[1].click()
        self.assertFalse(checkbox[1].is_selected())

    def tearDown(self):
        self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()
