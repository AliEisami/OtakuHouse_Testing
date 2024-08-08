from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class LoginAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def login(self, email, password):
        payload = {
            "username": email,
            "password": password
        }
        return self._request.post_request(url=f"{self._config['url']}{self._config['login_endpoint']}", json=payload)
