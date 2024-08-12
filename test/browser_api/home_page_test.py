import os
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.api.item_page_api import ItemPageAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.home_page import HomePage


class HomePageTest(unittest.TestCase):

    def test_high_rating_banner_displayed(self):
        """
        Test the display of a high rating banner on the home page. This test submits a review for a randomly
        selected item with a high rating (4 stars), and then verifies that the high rating banner is displayed
        on the home page.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        Logger(log_file_path).info("High Rating banner Displayed Test Started")
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        self.home_page = HomePage(self.driver)
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        ItemPageAPI(self.api_wrapper).review_item(26, self.config['review_rating'],
                                                  self.config['review_text'])
        self.driver.refresh()
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.home_page.HIGH_RATING_ITEMS))).is_displayed())
