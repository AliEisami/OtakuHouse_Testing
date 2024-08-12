import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from infra.utils import Utils
from logic.api.login_api import LoginAPI
from logic.api.registration_api import RegistrationAPI


class LoginAPITest(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        self.logger = Logger(log_file_path)
        self.api_wrapper = APIWrapper()

    def test_api_valid_login(self):
        """
            Test the API login functionality with valid credentials. This test first registers a new user,
            then attempts to log in with the same credentials. It ensures the login is successful and the
            response contains the expected username.
        """
        self.logger.info("API Valid Login Test Started")
        RegistrationAPI(self.api_wrapper).registration(self.config['email'], self.config['username'],
                                                       self.config['password'])
        login_api = LoginAPI(self.api_wrapper)
        response = login_api.login(self.config['email'], self.config['password'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.data['name'], self.config['username'])

    def test_api_invalid_login(self):
        """
        Test the API login functionality with invalid credentials. This test attempts to log in with
        a non-existent email and a randomly generated password. It ensures the API returns a 401 status
        with an appropriate error message indicating the credentials are invalid.
        """
        self.logger.info("API invalid Login Test Started")
        login_api = LoginAPI(self.api_wrapper)
        email = f"{Utils.generate_username(1)[0]}@gmail.com"
        password = Utils.generate_random_string(6, 9)
        response = login_api.login(email, password)
        self.assertEqual(response.status, 401)
        self.assertEqual(response.data['detail'], "No active account found with the given credentials")

