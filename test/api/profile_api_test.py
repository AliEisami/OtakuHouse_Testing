import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from logic.api.profile_api import ProfileAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage


class ProfileAPITest(unittest.TestCase):
    def test_api_profile_update_password(self):
        """
        Test the API functionality for updating the user password. This test sends a request to update the
        password for the user profile with the provided details, and verifies that the API responds with a
        successful status and the correct username in the response data.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        self.logger = Logger(log_file_path)
        self.logger.info("API profile update password Test Started")
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        self.base_page = BaseAppPage(self.driver)
        self.base_page.login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        profile_api = ProfileAPI(self.api_wrapper)
        response = profile_api.update_password(self.config['id'], self.config['username'],
                                               self.config['email'], self.config['password'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['name'], self.config['username'])
