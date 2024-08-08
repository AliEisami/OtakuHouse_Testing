import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.api.profile_api import ProfileAPI
from logic.api.registration_api import RegistrationAPI
from logic.browser.base_app_page import BaseAppPage
from logic.browser.login_page import LoginPage
from logic.browser.profile_page import ProfilePage


class ProfileTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.api_wrapper = APIWrapper()
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'], self.config['password'])
        self.base_page = BaseAppPage(self.driver)
        self.base_page.login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

    def test_profile_update_password(self):
        self.base_page.open_profile()
        profile_page = ProfilePage(self.driver)
        profile_page.fill_email_input(self.config['email'])
        profile_page.fill_password_input(self.config['new_password'])
        profile_page.fill_confirm_password_input(self.config['new_password'])
        profile_page.update_button_click()
        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, profile_page.EMAIL_INPUT)))
        self.assertEqual(email_input.get_attribute('value'), "")

    def test_api_profile_update_password(self):
        profile_api = ProfileAPI(self.api_wrapper)
        response = profile_api.update_password(self.config['id'], self.config['username'],
                                               self.config['email'], self.config['password'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['name'], self.config['username'])