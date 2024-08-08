import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.login_api import LoginAPI
from logic.api.registration_api import RegistrationAPI


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_wrapper = APIWrapper()
        self.registration_api = RegistrationAPI(self.api_wrapper)

    def test_api_valid_register(self):
        username = Utils.generate_username(1)[0]
        email = f"{username}@gmail.com"
        password = Utils.generate_random_string(5, 9)
        response = self.registration_api.registration(email, username, password)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['username'], f"{username}@gmail.com")

    def test_api_invalid_register(self):
        self.registration_api.registration(self.config['email'], self.config['username'], self.config['password'])
        response = self.registration_api.registration(self.config['email'], self.config['username'], self.config['password'])
        self.assertEqual(response.status, 400)
        self.assertEqual(response.data['detail'], "User with this email is already registered")
