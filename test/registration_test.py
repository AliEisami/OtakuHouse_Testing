import logging
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.registration_api import RegistrationAPI
from infra.logger import Logger


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_wrapper = APIWrapper()
        self.registration_api = RegistrationAPI(self.api_wrapper)

    def test_api_valid_register(self):
        """
            Test the API registration functionality with valid input by creating a new user.
            Ensure that the registration is successful and the response includes the correct username.
        """
        logging.info("API Valid Registration Test Started")
        username = Utils.generate_username(1)[0]
        email = f"{username}@gmail.com"
        password = Utils.generate_random_string(5, 9)
        response = self.registration_api.registration(email, username, password)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['username'], f"{username}@gmail.com")
        logging.info("Done\n_______________________________________________________")

    def test_api_invalid_register(self):
        """
            Test the API registration functionality with invalid input by attempting to register
            a user with an email that is already in use. Ensure that the API returns a 400 status
            and an appropriate error message.
        """
        logging.info("API Invalid Registration Test Started")
        self.registration_api.registration(self.config['email'], self.config['username'], self.config['password'])
        response = self.registration_api.registration(self.config['email'], self.config['username'], self.config['password'])
        self.assertEqual(response.status, 400)
        self.assertEqual(response.data['detail'], "User with this email is already registered")
        logging.info("Done\n_______________________________________________________")
