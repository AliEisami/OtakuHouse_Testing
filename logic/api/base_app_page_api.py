import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class BaseAppPageAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../config.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    def search(self, item_name):
        """
        Searches for products based on the provided item name.
        Args:
            item_name (str): The name of the item to search for.
        Returns:
            Response: The response object from the GET request.
        """
        return self._request.get_request(f"{self._config['url']}{self._config['get_product_endpoint']}"
                                         f"?keyword={item_name}&page=1")
