from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = '//div[@class="list-group-item"]//div[@class="row"]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def get_items_in_cart(self):
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.CART_ITEMS)))
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)
        return None