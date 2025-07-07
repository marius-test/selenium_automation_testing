import unittest

from selenium.webdriver.common.by import By

from utils.driver_factory import get_driver, quit_driver
from utils.waits import wait_for_presence

# TEST DATA
URL = "https://the-internet.herokuapp.com/dynamic_content"
expected_title = 'Dynamic Content'
expected_static_text_1 = "Accusantium eius ut architecto neque vel voluptatem vel nam eos minus ullam dolores voluptates enim sed voluptatem rerum qui sapiente nesciunt aspernatur et accusamus laboriosam culpa tenetur hic aut placeat error autem qui sunt."
expected_static_text_2 = "Omnis fugiat porro vero quas tempora quis eveniet ab officia cupiditate culpa repellat debitis itaque possimus odit dolorum et iste quibusdam quis dicta autem sint vel quo vel consequuntur dolorem nihil neque sunt aperiam blanditiis."
expected_static_image_1 = "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-7.jpg"
expected_static_image_2 = "https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-2.jpg"
images_numbers = [0, 1, 2, 3, 4, 5, 6, 7]
expected_dynamic_images = [f"https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-{number}.jpg" for number in images_numbers]


class TestDynamicContent(unittest.TestCase):
    SECTION_HEADER_LOCATOR = (By.TAG_NAME, "h3")

    def setUp(self):
        self.driver = get_driver()
        self.driver.get(URL)
        wait_for_presence(self.driver, self.SECTION_HEADER_LOCATOR)
        
    def test_title_is_correct(self):
        self.assertEqual(expected_title, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)
        self.driver.refresh()
        self.assertEqual(expected_title, self.driver.find_element(*self.SECTION_HEADER_LOCATOR).text)

    def test_static_text(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a").click()
        actual_static_text_1 = self.driver.find_element(By.CSS_SELECTOR, "#content > div:nth-child(1) > div.large-10.columns").text
        actual_static_text_2 = self.driver.find_element(By.CSS_SELECTOR, "#content > div:nth-child(4) > div.large-10.columns").text
        self.assertEqual(expected_static_text_1, actual_static_text_1)
        self.assertEqual(expected_static_text_2, actual_static_text_2)
        self.driver.refresh()
        self.assertEqual(expected_static_text_1, actual_static_text_1)
        self.assertEqual(expected_static_text_2, actual_static_text_2)

    def test_static_images(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > div > p:nth-child(3) > a").click()
        actual_image_1 = self.driver.find_element(By.CSS_SELECTOR, '#content > div:nth-child(1) > div.large-2.columns > img').get_attribute('src')
        actual_image_2 = self.driver.find_element(By.CSS_SELECTOR, '#content > div:nth-child(4) > div.large-2.columns > img').get_attribute('src')
        self.assertEqual(expected_static_image_1, actual_image_1)
        self.assertEqual(expected_static_image_2, actual_image_2)
        self.driver.refresh()
        self.assertEqual(expected_static_image_1, actual_image_1)
        self.assertEqual(expected_static_image_2, actual_image_2)
 
    def test_dynamic_text(self):
        self.assertIsInstance(self.driver.find_element(By.CSS_SELECTOR, "#content > div:nth-child(1) > div.large-10.columns").text, str)
        self.assertIsInstance(self.driver.find_element(By.CSS_SELECTOR, "#content > div:nth-child(4) > div.large-10.columns").text, str)
        self.assertIsInstance(self.driver.find_element(By.CSS_SELECTOR, "#content > div:nth-child(7) > div.large-10.columns").text, str)

    def test_dynamic_images(self):
        images = self.driver.find_elements(By.TAG_NAME, "img")
        for image in images:
            with self.subTest(image=image):
                self.assertEqual(image.tag_name, "img")
    
    def tearDown(self):
        quit_driver(self.driver)
