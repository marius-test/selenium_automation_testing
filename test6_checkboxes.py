import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = Service("C:\\Users\\marius\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
text = "checkbox 1\ncheckbox 2"


class Checkboxes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="//a[normalize-space()='Checkboxes']").click()

    def test_text(self):
        driver = self.driver
        checkbox_string = driver.find_element(by=By.TAG_NAME, value="form").text
        self.assertEqual(checkbox_string, text)

    def test_check(self):
        driver = self.driver
        checkbox = driver.find_elements(by=By.TAG_NAME, value="input")
        if checkbox[0].is_selected() == False:
            checkbox[0].click()
        self.assertTrue(checkbox[0].is_selected())
        if checkbox[1].is_selected() == False:
            checkbox[1].click()
        self.assertTrue(checkbox[1].is_selected())

    def test_uncheck(self):
        driver = self.driver
        checkbox = driver.find_elements(by=By.TAG_NAME, value="input")
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
