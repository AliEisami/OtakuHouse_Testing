import os
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.api.order_api import OrderAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage
from logic.browser.order_page import OrderPage
from logic.browser.profile_page import ProfilePage


class OrderTest(unittest.TestCase):

    def test_order_pay(self):
        """
        Test the functionality of processing an order payment via the UI. This test places an order, navigates to the
        profile to open the last order, and then completes the payment process using the provided credit card details.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        Logger(log_file_path).info("Order Payment Test Started")
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        self.order_api = OrderAPI(self.api_wrapper)
        self.base_page = BaseAppPage(self.driver)
        self.base_page.login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        self.order_api.place_an_order(self.config['order'])
        self.base_page.open_profile()
        ProfilePage(self.driver).open_last_order()
        order_page = OrderPage(self.driver)
        order_page.click_credit_card_button()
        order_page.payment_flow(self.config['payment_details'])
        print(self.config['payment_details'])
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, order_page.PAID_ALERT))).is_displayed())
