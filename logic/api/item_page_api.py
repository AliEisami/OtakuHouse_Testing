import os

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class ItemPageAPI:

    def __init__(self, request: APIWrapper):
        self._request = request
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../../config.json')
        self._config = ConfigProvider().load_from_file(self._config_file_path)

    def review_item(self, product, rating, review):
        """
        Submits a review for a product with the given rating and comment.
        Args:
            product (int): The product ID to review.
            rating (int): The rating given to the product (e.g., 1-5).
            review (str): The review comment for the product.
        Returns:
            Response: The response object from the POST request.
        """
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
