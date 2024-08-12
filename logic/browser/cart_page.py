from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = '//div[@class="list-group-item"]//div[@class="row"]'
    ITEM_NAME = '//div[@m="3"]//a'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def get_items_in_cart(self):
        """
        Retrieves all items currently in the cart.
        Returns:
            list: A list of WebElement objects representing the items in the cart, or None if no items are found.
        """
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.CART_ITEMS)))
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def get_item_name(self):
        try:
            return WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.ITEM_NAME))).text
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)
            return None
