import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage
from logic.browser.base_app_page import BaseAppPage


class HomePage(BasePage):

    ALL_ITEMS_IN_PAGE = '//div[@class="col-xl-3 col-lg-4 col-md-6 col-sm-12"]'
    HIGH_RATING_ITEMS = '//div[@class="active carousel-item"]'
    HIGH_RATING_BANNER_PREV = '//a[@class="carousel-control-prev"]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def select_and_open_item(self, item_number):
        """
        Selects an item by its number and opens its details page.
        Args:
            item_number (int): The index of the item to select (0-based index).
        """
        try:
            items = WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.ALL_ITEMS_IN_PAGE)))
            self._driver.execute_script("arguments[0].scrollIntoView(true);", items[int(item_number)-19])
            time.sleep(1)
            items[int(item_number)-19].click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)
