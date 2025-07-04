import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import get_driver, quit_driver

# test data
url = "https://the-internet.herokuapp.com/"


class TestAddRemoveElement(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/add_remove_elements/']").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))

    def test_add_element(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
        self.assertEqual("Delete", self.driver.find_element(By.CSS_SELECTOR, ".added-manually").text)

    def test_remove_element(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
        self.assertEqual("Delete", self.driver.find_element(By.CSS_SELECTOR, ".added-manually").text)
        self.driver.find_element(By.CSS_SELECTOR, ".added-manually").click()
        self.assertTrue(WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".added-manually"))))
        # self.assertFalse(driver.find_element(By.CSS_SELECTOR, ".added-manually").is_displayed())

    def tearDown(self):
        quit_driver(self.driver)
