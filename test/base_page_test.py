import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.api.api_wrapper import APIWrapper
from infra.browser.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.api.base_app_page_api import BaseAppPageAPI
from logic.browser.base_app_page import BaseAppPage


class BasePageTest(unittest.TestCase):

    ITEMS_PATH = '//div[@class="card-title"]'

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_wrapper = APIWrapper()
        self.base_app_page_api = BaseAppPageAPI(self.api_wrapper)

    def test_api_search(self):
        response = self.base_app_page_api.search(self.config['search_item_name'])
        self.assertTrue(response.ok)
        self.assertEqual(response.status, 200)
        self.assertGreaterEqual(len(response.data['products']), 1)

    def test_ui_search(self):
        driver = self.browser.get_driver(self.config['url'])
        base_app_page = BaseAppPage(driver)
        base_app_page.fill_search_input(self.config['search_item_name'])
        base_app_page.search_button_click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.ITEMS_PATH)))
        items = driver.find_elements(By.XPATH, self.ITEMS_PATH)
        response = self.base_app_page_api.search(self.config['search_item_name'])
        self.assertEqual(len(items), len(response.data['products']))
