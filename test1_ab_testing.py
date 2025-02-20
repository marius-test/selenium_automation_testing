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

# test data
expected_title = ["A/B Test Control", "A/B Test Variation 1"]
expected_text = "Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."


class TestABTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
    
    def test_title_is_correct(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/abtest']").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        self.assertIn(expected_title, self.driver.find_element(By.TAG_NAME, "h3").text)
                         
    def test_text_is_correct(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/abtest']").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
        self.assertEqual(expected_text, self.driver.find_element(By.TAG_NAME, "p").text)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
