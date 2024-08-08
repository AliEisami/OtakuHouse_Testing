from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class BaseAppPageAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def search(self, item_name):
        return self._request.get_request(f"{self._config['url']}{self._config['get_product_endpoint']}"
                                         f"?keyword={item_name}&page=1")
