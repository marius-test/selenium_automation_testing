import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"


class AddRemoveElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()

    def test_add_element(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/add_remove_elements/']").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".added-manually").text, "Delete")

    def test_remove_element(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/add_remove_elements/']").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".added-manually").text, "Delete")
        self.driver.find_element(By.CSS_SELECTOR, ".added-manually").click()
        self.assertTrue(WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".added-manually"))))
        # self.assertFalse(driver.find_element(By.CSS_SELECTOR, ".added-manually").is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
