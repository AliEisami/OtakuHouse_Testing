import os
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage


class LoginTest(unittest.TestCase):
    def test_ui_valid_login(self):
        """
        Test the UI login functionality with valid credentials. This test navigates to the login page,
        performs a login with valid credentials, and verifies that the user is redirected to the home page.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        Logger(log_file_path).info("UI Valid Login Test Started")
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        driver = self.browser.get_driver(self.config['url'])
        BaseAppPage(driver).login_button_click()
        login_page = LoginPage(driver)
        login_page.login_flow(self.config['email'], self.config['password'])
        WebDriverWait(driver, 10).until(EC.url_changes(f"{self.config['url']}/#/login"))
        self.assertEqual(driver.current_url, f"{self.config['url']}/#/")
