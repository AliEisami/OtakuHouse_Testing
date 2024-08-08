from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


class BaseAppPage(BasePage):

    HOME_BUTTON = '//a[@class="active navbar-brand"]'
    SEARCH_INPUT = '//input[@class="mr-sm-2 ml-sm-5 form-control"]'
    SEARCH_BUTTON = '//button[@class="p-2 mx-sm-2 btn btn-outline-success"]'
    CART_BUTTON = '//a[@data-rb-event-key="#/cart"]'
    LOGIN_BUTTON = '//a[@data-rb-event-key="#/login"]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def home_button_click(self):
        """ Clicks on the Home button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.HOME_BUTTON)))
        try:
            home_button = self._driver.find_element(By.XPATH, self.HOME_BUTTON)
            home_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_search_input(self, item_name):
        """ Enter String to Search input. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_INPUT)))
        try:
            search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
            search_input.send_keys(item_name)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def search_button_click(self):
        """ Clicks on the search button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_BUTTON)))
        try:
            search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
            search_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def cart_button_click(self):
        """ Clicks on the cart button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.CART_BUTTON)))
        try:
            cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
            cart_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def login_button_click(self):
        """ Clicks on the login button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        try:
            login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
            login_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def search_flow(self, item_name):
        self.fill_search_input(item_name)
        self.search_button_click()
