import os
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.base_app_page_api import BaseAppPageAPI
from infra.logger import Logger


class BasePageAPITest(unittest.TestCase):

    ITEMS_PATH = '//div[@class="card-title"]'

    def test_api_search(self):
        """
            Test the API search functionality by verifying that a search returns a successful response
            with a status code of 200 and at least one product in the results.
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(base_dir, '../../config.json')
        self.config = ConfigProvider().load_from_file(self.config_file_path)
        log_file_path = os.path.join(base_dir, '../../logger.log')
        self.logger = Logger(log_file_path)
        self.logger.info("API Search Test Started")
        self.api_wrapper = APIWrapper()
        base_app_page_api = BaseAppPageAPI(self.api_wrapper)
        response = base_app_page_api.search(self.config['search_item_name'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertGreaterEqual(len(response.data['products']), 1)
