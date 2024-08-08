import time
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.item_page_api import ItemPageAPI
from logic.browser.cart_page import CartPage
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage


class ItemPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.home_page = HomePage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.api_wrapper = APIWrapper()
        self.item_pade_api = ItemPageAPI(self.api_wrapper)

    def test_api_review_successfully(self):
        response = self.item_pade_api.review_item(26, self.config['review_rating'], self.config['review_text'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertGreaterEqual(response.data, "Review Added")

    def test_api_review_unsuccessfully(self):
        number = Utils.random_number(11, 25)
        self.item_pade_api.review_item(number, self.config['review_rating'], self.config['review_text'])
        response = self.item_pade_api.review_item(number, self.config['review_rating'], self.config['review_text'])
        self.assertEqual(response.status, 400)
        self.assertGreaterEqual(response.data['detail'], "Product already reviewed")

    def test_add_item_to_cart(self):
        self.home_page.select_and_open_item(3)
        self.item_page.add_item_to_cart_flow(3)
        self.assertTrue(CartPage(self.driver).get_items_in_cart() is not None)
