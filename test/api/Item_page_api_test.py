import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.logger import Logger
from infra.utils import Utils
from logic.api.item_page_api import ItemPageAPI


class ItemPageAPITest(unittest.TestCase):

    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        self.logger = Logger(log_file_path)
        self.api_wrapper = APIWrapper()
        self.item_page_api = ItemPageAPI(self.api_wrapper)

    def test_api_review_successfully(self):
        """
        Test the API functionality for successfully adding a review. This test submits a review for an item
        with a specified rating and review text, and verifies that the API response indicates the review was
        added successfully.
        """
        self.logger.info("API Add Review Successfully Test Started")
        response = self.item_page_api.review_item(Utils.random_number(16, 25), self.config['review_rating'],
                                                  self.config['review_text'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertGreaterEqual(response.data, "Review Added")

    def test_api_review_unsuccessfully(self):
        """
        Test the API functionality for unsuccessfully adding a review. This test first submits a review for an item,
        and then attempts to submit another review for the same item, expecting the API to return a 400 status
        with an error message indicating that the product has already been reviewed.
        """
        self.logger.info("API Add Review Unsuccessfully Test Started")
        number = Utils.random_number(11, 15)
        self.item_page_api.review_item(number, self.config['review_rating'], self.config['review_text'])
        response = self.item_page_api.review_item(number, self.config['review_rating'], self.config['review_text'])
        self.assertEqual(response.status, 400)
        self.assertGreaterEqual(response.data['detail'], "Product already reviewed")