from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ProfileAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def update_password(self, id, name, email, password):
        """
        Updates the password for a user with the given ID, name, and email.
        Args:
            id (str): The user ID.
            name (str): The username of the user.
            email (str): The email address of the user.
            password (str): The new password to set for the user.
        Returns:
            Response: The response object from the PUT request.
        """
        payload = {
            "id": id,
            "name": name,
            "email": email,
            "password": password
        }
        headers = {
            "Authorization": self._config['Authorization']
        }
        return self._request.put_request(url=f"{self._config['url']}{self._config['password_update_endpoint']}",
                                         headers=headers, json=payload)
