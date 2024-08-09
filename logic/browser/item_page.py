from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.browser.base_app_page import BaseAppPage
from selenium.webdriver.support.ui import Select


class ItemPage(BaseAppPage):
    ADD_TO_CART_BUTTON = '//button[@class="w-100 btn btn-primary"]'
    QTY_SELECT = '//div[@class="my-1 col-auto"]//select[@class="form-control"]'

    def __init__(self, driver):
        """
            Initializes an instance of LoginPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def add_to_cart_button_click(self):
        """ Clicks on the add to cart button. """
        try:
            add_to_cart = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.ADD_TO_CART_BUTTON)))
            add_to_cart.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def select_quantity(self, quantity):
        """
        Selects the quantity of an item from a dropdown menu.
        Args:
            quantity (int): The quantity to select (1-based index).
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.QTY_SELECT)))
        try:
            select_quantity = Select(self._driver.find_element(By.XPATH, self.QTY_SELECT))
            select_quantity.select_by_index(quantity-1)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def add_item_to_cart_flow(self, quantity):
        """
        Selects the item quantity and clicks the "Add to Cart" button.
        Args:
            quantity (int): The quantity of the item to add to the cart.
        """
        self.select_quantity(quantity)
        self.add_to_cart_button_click()