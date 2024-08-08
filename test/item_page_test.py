import logging
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.item_page_api import ItemPageAPI
from logic.browser.cart_page import CartPage
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage
from infra.logger import Logger


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
        """
        Test the API functionality for successfully adding a review. This test submits a review for an item
        with a specified rating and review text, and verifies that the API response indicates the review was
        added successfully.
        """
        logging.info("API Add Review Successfully Test Started")
        response = self.item_pade_api.review_item(26, self.config['review_rating'], self.config['review_text'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertGreaterEqual(response.data, "Review Added")
        logging.info("Done\n_______________________________________________________")

    def test_api_review_unsuccessfully(self):
        """
        Test the API functionality for unsuccessfully adding a review. This test first submits a review for an item,
        and then attempts to submit another review for the same item, expecting the API to return a 400 status
        with an error message indicating that the product has already been reviewed.
        """
        logging.info("API Add Review Unsuccessfully Test Started")
        number = Utils.random_number(11, 25)
        self.item_pade_api.review_item(number, self.config['review_rating'], self.config['review_text'])
        response = self.item_pade_api.review_item(number, self.config['review_rating'], self.config['review_text'])
        self.assertEqual(response.status, 400)
        self.assertGreaterEqual(response.data['detail'], "Product already reviewed")
        logging.info("Done\n_______________________________________________________")

    def test_add_item_to_cart(self):
        """
        Test the UI functionality for adding an item to the cart. This test selects and opens an item from the home page,
        adds it to the cart, and verifies that the item appears in the cart.
        """
        logging.info("Add Item To Cart Test Started")
        self.home_page.select_and_open_item(3)
        self.item_page.add_item_to_cart_flow(3)
        self.assertTrue(CartPage(self.driver).get_items_in_cart() is not None)
        logging.info("Done\n_______________________________________________________")
