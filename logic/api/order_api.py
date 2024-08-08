from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class OrderAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def place_an_order(self, payload):
        payload = payload
        headers = {
            "Authorization": self._config['Authorization']
        }
        return self._request.post_request(url=f"{self._config['url']}{self._config['order_endpoint']}",
                                          headers=headers, json=payload)