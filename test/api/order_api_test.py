import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.api.order_api import OrderAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage


class OrderAPITest(unittest.TestCase):

    def test_api_place_order(self):
        """
        Test the API functionality for placing an order. This test sends a request to place an order with the
        specified order details, and verifies that the API responds with a successful status and that the
        order details in the response match the submitted order.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        self.logger = Logger(log_file_path)
        self.logger.info("API place order Test Started")
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        self.order_api = OrderAPI(self.api_wrapper)
        BaseAppPage(self.driver).login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        response = self.order_api.place_an_order(self.config['order'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['orderItems'][0]['product'], self.config['order']['orderItems'][0]['product'])
