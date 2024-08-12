import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from infra.utils import Utils
from logic.api.registration_api import RegistrationAPI


class RegistrationAPITest(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        self.logger = Logger(log_file_path)
        self.api_wrapper = APIWrapper()
        self.registration_api = RegistrationAPI(self.api_wrapper)

    def test_api_valid_register(self):
        """
            Test the API registration functionality with valid input by creating a new user.
            Ensure that the registration is successful and the response includes the correct username.
        """
        self.logger.info("API Valid Registration Test Started")
        username = Utils.generate_username(1)[0]
        email = f"{username}@gmail.com"
        password = Utils.generate_random_string(5, 9)
        response = self.registration_api.registration(email, username, password)
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['username'], f"{username}@gmail.com")

    def test_api_invalid_register(self):
        """
            Test the API registration functionality with invalid input by attempting to register
            a user with an email that is already in use. Ensure that the API returns a 400 status
            and an appropriate error message.
        """
        self.logger.info("API Invalid Registration Test Started")
        self.registration_api.registration(self.config['email'], self.config['username'], self.config['password'])
        response = self.registration_api.registration(self.config['email'], self.config['username'],
                                                      self.config['password'])
        self.assertEqual(response.status, 400)
        self.assertEqual(response.data['detail'], "User with this email is already registered")
