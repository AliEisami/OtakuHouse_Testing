import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class LoginAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../config.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    def login(self, email, password):
        """
        Authenticates a user with the provided email and password.
        Args:
            email (str): The email address of the user.
            password (str): The password for the user account.
        Returns:
            Response: The response object from the POST request.
        """
        payload = {
            "username": email,
            "password": password
        }
        return self._request.post_request(url=f"{self._config['url']}{self._config['login_endpoint']}", json=payload)
