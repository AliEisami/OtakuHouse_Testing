from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ItemPageAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def review_item(self, product, rating, review):
        payload = {
            "rating": rating,
            "comment": review
        }
        headers = {
            "Authorization": self._config['Authorization']
        }
        return self._request.post_request(
            url=f"{self._config['url']}{self._config['get_product_endpoint']}{product}{self._config['review_endpoint']}",
            headers=headers, json=payload)
