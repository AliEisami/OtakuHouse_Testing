from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class RegistrationAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def registration(self, email, username, password):
        """
        Registers a new user with the provided email, username, and password.
        Args:
            email (str): The email address of the user.
            username (str): The username of the user.
            password (str): The password for the user account.
        Returns:
            Response: The response object from the POST request.
        """
        payload = {
            "email": email,
            "name": username,
            "password": password
        }
        return self._request.post_request(url=f"{self._config['url']}{self._config['register_endpoint']}", json=payload)
