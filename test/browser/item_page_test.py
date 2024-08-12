import os
import unittest
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from infra.utils import Utils
from logic.browser.cart_page import CartPage
from logic.browser.home_page import HomePage
from logic.browser.item_page import ItemPage


class ItemPageTest(unittest.TestCase):
    def test_add_item_to_cart(self):
        """
        Test the UI functionality for adding an item to the cart. This test selects and opens an item from the home page,
        adds it to the cart, and verifies that the item appears in the cart.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        Logger(log_file_path).info("Add Item To Cart Test Started")
        self.driver = self.browser.get_driver(self.config['url'])
        self.home_page = HomePage(self.driver)
        self.home_page.select_and_open_item(Utils.random_number(19, 26))
        self.item_page = ItemPage(self.driver)
        item_name = self.item_page.get_item_name()
        self.item_page.add_item_to_cart_flow(Utils.random_number(1, 3))
        cart_item_name = CartPage(self.driver).get_item_name()
        self.assertEqual(item_name.lower(), cart_item_name.lower())
