from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class ProfilePage(BasePage):

    CART_ITEMS = '//div[@class="list-group-item"]//div[@class="row"]'
    ITEM_DETAILS_BUTTON = '//a[text() = "Details"]'
    EMAIL_INPUT = '//input[@id="email"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    CONFIRM_PASSWORD_INPUT = '//input[@id="passwordConfirm"]'
    UPDATE_BUTTON = '//button[text()="Update"]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def get_orders(self):
        try:
            return WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.CART_ITEMS)))
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)
        return None

    def open_last_order(self):
        try:
            orders = WebDriverWait(self._driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, self.ITEM_DETAILS_BUTTON)))
            order = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((orders[len(orders)-1])))
            order.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_email_input(self, email):
        email_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.EMAIL_INPUT)))
        email_input.send_keys(email)

    def fill_password_input(self, password):
        password_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PASSWORD_INPUT)))
        password_input.send_keys(password)

    def fill_confirm_password_input(self, confirm_password):
        confirm_password_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_PASSWORD_INPUT)))
        confirm_password_input.send_keys(confirm_password)

    def update_button_click(self):
        update_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.UPDATE_BUTTON)))
        update_button.click()

    def update_password_flow(self, email, password, confirm_password):
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.fill_confirm_password_input(confirm_password)
