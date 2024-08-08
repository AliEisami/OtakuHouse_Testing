from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ProfileAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def update_password(self, id, name, email, password):
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
