from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class RegistrationAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def registration(self, email, username, password):
        payload = {
            "email": email,
            "name": username,
            "password": password
        }
        return self._request.post_request(url=f"{self._config['url']}{self._config['register_endpoint']}", json=payload)
