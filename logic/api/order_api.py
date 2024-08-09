import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class OrderAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../config.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    def place_an_order(self, payload):
        """
        Places an order with the given payload.
        Args:
            payload (dict): The order details to be sent in the request body.
        Returns:
            Response: The response object from the POST request.
        """
        payload = payload
        headers = {
            "Authorization": self._config['Authorization']
        }
        return self._request.post_request(url=f"{self._config['url']}{self._config['order_endpoint']}",
                                          headers=headers, json=payload)