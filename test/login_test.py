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
        self.config = ConfigProvider.load_from_file()
        self.api_wrapper = APIWrapper()
        self.login_api = LoginAPI(self.api_wrapper)

    def test_api_valid_login(self):
        RegistrationAPI.registration(self.config['email'], self.config['username'], self.config['password'])
        response = self.login_api.login(self.config['email'], self.config['password'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['name'], self.config['username'])

    def test_api_invalid_login(self):
        email = f"{Utils.generate_username(1)[0]}@gmail.com"
        password = Utils.generate_random_string(6, 9)
        response = self.login_api.login(email, password)
        self.assertEqual(response.status, 401)
        self.assertEqual(response.data['detail'], "No active account found with the given credentials")

    # def test_ui_valid_login(self):
    #     driver = self.browser.get_driver(self.config['url'])
    #     BaseAppPage(driver).login_button_click()
    #     login_page = LoginPage(driver)
    #     login_page.login_flow(self.config['email'], self.config['password'])
    #     WebDriverWait(driver, 5).until(EC.url_matches(f"{self.config['url']}/#/"))
    #     self.assertEqual(driver.current_url, f"{self.config['url']}/#/")
