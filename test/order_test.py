import logging
import unittest
from selenium.webdriver.common.by import By
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.api.order_api import OrderAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage
from logic.browser.order_page import OrderPage
from logic.browser.profile_page import ProfilePage
from infra.logger import Logger


class OrderTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'], self.config['password'])
        self.order_api = OrderAPI(self.api_wrapper)
        self.base_page = BaseAppPage(self.driver)
        self.base_page.login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

    def test_api_place_order(self):
        """
        Test the API functionality for placing an order. This test sends a request to place an order with the
        specified order details, and verifies that the API responds with a successful status and that the
        order details in the response match the submitted order.
        """
        logging.info("API Place Order Test Started")
        response = self.order_api.place_an_order(self.config['order'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['orderItems'][0]['product'], self.config['order']['orderItems'][0]['product'])
        logging.info("Done\n_______________________________________________________")

    def test_order_pay(self):
        """
        Test the functionality of processing an order payment via the UI. This test places an order, navigates to the
        profile to open the last order, and then completes the payment process using the provided credit card details.
        """
        logging.info("Order Payment Test Started")
        self.order_api.place_an_order(self.config['order'])
        self.base_page.open_profile()
        ProfilePage(self.driver).open_last_order()
        order_page = OrderPage(self.driver)
        order_page.click_credit_card_button()
        order_page.payment_flow(self.config['payment_details']['Credit_Card_Number'],
                                self.config['payment_details']['Expiry_Date'],
                                self.config['payment_details']['cvv'],
                                self.config['payment_details']['First_Name'],
                                self.config['payment_details']['Last_Name'],
                                self.config['payment_details']['street'],
                                self.config['payment_details']['city'],
                                self.config['payment_details']['zipcode'],
                                self.config['payment_details']['Phone'],
                                self.config['payment_details']['email'])
        iframe = self.driver.find_elements(By.XPATH, order_page.IFRAME)
        self.assertTrue(len(iframe) == 0)
        logging.info("Done\n_______________________________________________________")
