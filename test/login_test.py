import logging
import os
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.login_api import LoginAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        self.api_wrapper = APIWrapper()

    def test_api_valid_login(self):
        """
            Test the API login functionality with valid credentials. This test first registers a new user,
            then attempts to log in with the same credentials. It ensures the login is successful and the
            response contains the expected username.
        """
        logging.info("API Valid Login Test Started")
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'], self.config['password'])
        login_api = LoginAPI(self.api_wrapper)
        response = login_api.login(self.config['email'], self.config['password'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['name'], self.config['username'])
        logging.info("Done\n_______________________________________________________")

    def test_api_invalid_login(self):
        """
        Test the API login functionality with invalid credentials. This test attempts to log in with
        a non-existent email and a randomly generated password. It ensures the API returns a 401 status
        with an appropriate error message indicating the credentials are invalid.
        """
        logging.info("API invalid Login Test Started")
        login_api = LoginAPI(self.api_wrapper)
        email = f"{Utils.generate_username(1)[0]}@gmail.com"
        password = Utils.generate_random_string(6, 9)
        response = login_api.login(email, password)
        self.assertEqual(response.status, 401)
        self.assertEqual(response.data['detail'], "No active account found with the given credentials")
        logging.info("Done\n_______________________________________________________")

    def test_ui_valid_login(self):
        """
        Test the UI login functionality with valid credentials. This test navigates to the login page,
        performs a login with valid credentials, and verifies that the user is redirected to the home page.
        """
        logging.info("UI Valid Login Test Started")
        driver = self.browser.get_driver(self.config['url'])
        BaseAppPage(driver).login_button_click()
        login_page = LoginPage(driver)
        login_page.login_flow(self.config['email'], self.config['password'])
        WebDriverWait(driver, 10).until(EC.url_changes(f"{self.config['url']}/#/login"))
        self.assertEqual(driver.current_url, f"{self.config['url']}/#/")
        logging.info("Done\n_______________________________________________________")
