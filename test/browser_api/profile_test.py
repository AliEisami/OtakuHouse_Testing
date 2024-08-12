import os
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.jira_client_setup import create_issue
from infra.logger import Logger
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage
from logic.browser.profile_page import ProfilePage


class ProfileTest(unittest.TestCase):
    project_key = 'OHTP'

    def test_profile_update_password(self):
        """
        Test the UI functionality for updating the user password. This test navigates to the profile page, fills
        in the necessary fields to update the password, and clicks the update button.
        """
        self.browser = BrowserWrapper()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        Logger(log_file_path).info("UI profile update password Test Started")
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        self.base_page = BaseAppPage(self.driver)
        self.base_page.login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        self.base_page.open_profile()
        profile_page = ProfilePage(self.driver)
        try:
            profile_page.fill_email_input(self.config['email'])
            profile_page.fill_password_input(self.config['new_password'])
            profile_page.fill_confirm_password_input(self.config['new_password'])
            profile_page.update_button_click()

            email_input = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, profile_page.EMAIL_INPUT))
            )
            self.assertEqual(email_input.get_attribute('value'), "")
        except AssertionError as e:
            summary = "UI Test Failure: Profile Update Password"
            description = (
                f"Test failed during the profile password update.\n"
                f"Steps to reproduce:\n"
                f"1. Navigate to the profile page.\n"
                f"2. Fill in email and password fields.\n"
                f"3. Click the update button.\n"
                f"Expected result: Email input should be empty after update.\n"
                f"Error: {str(e)}"
            )
            create_issue(summary, description, self.project_key)
            raise
