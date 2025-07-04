import unittest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# PATH = Service("C:\\Users\\marius\\webdriver\\chromedriver.exe")
chrome_service = Service(ChromeDriverManager().install())
url = "https://the-internet.herokuapp.com/"

# test data
expected_header = "Disappearing Elements"
expected_paragraph = "This example demonstrates when elements on a page change by disappearing/reappearing on each page load."
expected_buttons = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
expected_footer = "Powered by Elemental Selenium"
expected_footer_link = "http://elementalselenium.com/"
expected_url = x = ["", "about/", "contact-us/", "portfolio/", "gallery/"]
expected_response = ["<Response [200]>", "<Response [404]>", "<Response [404]>", "<Response [404]>"]


class TestDisappearingElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[9]/a").click()

    def test_header_and_paragraph(self):
        self.assertEqual(expected_header, self.driver.find_element(By.TAG_NAME, "h3").text)
        self.assertEqual(expected_paragraph, self.driver.find_element(By.TAG_NAME, "p").text)
    
    def test_buttons_text(self):
        list_of_buttons = self.driver.find_elements(By.TAG_NAME, "li")
        i = 0
        for button in list_of_buttons:
            self.assertEqual(expected_buttons[i], list_of_buttons[i].text)
            i += 1

    def test_buttons_redirect(self):
        list_of_buttons = self.driver.find_elements(By.TAG_NAME, "a")
        for i in range(0, 4):
            self.assertEqual(f"https://the-internet.herokuapp.com/{x[i]}", list_of_buttons[i + 1].get_attribute("href"))
            list_of_buttons[i + 1].click()
            response = requests.get(self.driver.current_url, stream=True)
            self.assertEqual(expected_response[i], str(response))
            self.driver.back()
      
    def test_missing_button(self):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/ul/li[5]/a")))
        except TimeoutException:
            button_is_displayed = 'No'
        else:
            button_is_displayed = 'Yes'
        finally:
            self.assertTrue(button_is_displayed == 'Yes')

    def test_footer(self):
        footer = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div")
        link = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/a")
        self.assertEqual(expected_footer, footer.text)
        self.assertEqual(expected_footer_link, link.get_attribute("href"))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
