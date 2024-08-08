import logging
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.item_page_api import ItemPageAPI
from logic.browser.home_page import HomePage
from infra.logger import Logger


class HomePageTest(unittest.TestCase):

    ITEMS_PATH = '//div[@class="card-title"]'

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        self.home_page = HomePage(self.driver)

    def test_high_rating_banner_displayed(self):
        """
        Test the display of a high rating banner on the home page. This test submits a review for a randomly
        selected item with a high rating (4 stars), and then verifies that the high rating banner is displayed
        on the home page.
        """
        logging.info("High Rating banner Displayed Test Started")
        ItemPageAPI(self.api_wrapper).review_item(Utils.random_number(11, 25), 4, self.config['review_text'])
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.home_page.HIGH_RATING_ITEMS))).is_displayed())
        logging.info("Done\n_______________________________________________________")
