import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = Service("C:\\Users\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"


class AddRemoveElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()

    def test_add_element(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/add_remove_elements/']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        driver.find_element(by=By.CSS_SELECTOR, value="button[onclick='addElement()']").click()
        self.assertEqual(driver.find_element(by=By.CSS_SELECTOR, value=".added-manually").text, "Delete")

    def test_remove_element(self):
        driver = self.driver
        driver.find_element(by=By.CSS_SELECTOR, value="a[href='/add_remove_elements/']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        driver.find_element(by=By.CSS_SELECTOR, value="button[onclick='addElement()']").click()
        self.assertEqual(driver.find_element(by=By.CSS_SELECTOR, value=".added-manually").text, "Delete")
        driver.find_element(by=By.CSS_SELECTOR, value=".added-manually").click()
        self.assertTrue(WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".added-manually"))))
        # self.assertFalse(driver.find_element(by=By.CSS_SELECTOR, value=".added-manually").is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
