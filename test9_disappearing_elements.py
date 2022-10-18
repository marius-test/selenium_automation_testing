import unittest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


PATH = Service("C:\\Users\\mariu\\chromedriver.exe")
url = "https://the-internet.herokuapp.com/"
header = "Disappearing Elements"
paragraph = "This example demonstrates when elements on a page change by disappearing/reappearing on each page load."
expected_buttons = ["Home", "About", "Contact Us", "Portfolio", "Gallery"]
expected_footer = "Powered by Elemental Selenium"
expected_footer_link = "http://elementalselenium.com/"
expected_url = x = ["", "about/", "contact-us/", "portfolio/", "gallery/"]
expected_response = ["<Response [200]>", "<Response [404]>", "<Response [404]>", "<Response [404]>"]


class DisappearingElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=PATH)
        driver = self.driver
        driver.get(url)
        driver.maximize_window()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/ul/li[9]/a").click()

    def test_header_and_paragraph(self):
        driver = self.driver
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="h3").text, header)
        self.assertEqual(driver.find_element(by=By.TAG_NAME, value="p").text, paragraph)
    
    def test_buttons_text(self):
        driver = self.driver
        list_of_buttons = driver.find_elements(by=By.TAG_NAME, value="li")
        i = 0
        for button in list_of_buttons:
            self.assertEqual(list_of_buttons[i].text, expected_buttons[i])
            i += 1

    def test_buttons_redirect(self):
        driver = self.driver
        list_of_buttons = driver.find_elements(by=By.TAG_NAME, value="a")
        for i in range(0, 4):
            self.assertEqual(list_of_buttons[i + 1].get_attribute("href"), f"https://the-internet.herokuapp.com/{x[i]}")
            list_of_buttons[i + 1].click()
            response = requests.get(driver.current_url, stream=True)
            self.assertEqual(str(response), expected_response[i])
            driver.back()
      
    def test_missing_button(self):
        driver = self.driver
        try:
            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/ul/li[5]/a")))
        except TimeoutException:
            button_is_displayed = 'No'
        else:
            button_is_displayed = 'Yes'
        finally:
            self.assertTrue(button_is_displayed == 'Yes')

    def test_footer(self):
        driver = self.driver
        footer = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div")
        link = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/a")
        self.assertEqual(footer.text, expected_footer)
        self.assertEqual(link.get_attribute("href"), expected_footer_link)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
