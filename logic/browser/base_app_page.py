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
    LOGOUT_BUTTON = '//a[text()="Logout"]'
    USERNAME_DROPDOWN = '//a[@id="username"]'
    PROFILE_BUTTON = '//a[@href="#/profile"]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def home_button_click(self):
        """
        Clicks the home button to navigate to the homepage.
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.HOME_BUTTON)))
        try:
            home_button = self._driver.find_element(By.XPATH, self.HOME_BUTTON)
            home_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_search_input(self, item_name):
        """
        Enters the specified item name into the search input field.
        Args:
            item_name (str): The name of the item to search for.
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_INPUT)))
        try:
            search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
            search_input.send_keys(item_name)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def search_button_click(self):
        """
        Clicks the search button to initiate a search.
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_BUTTON)))
        try:
            search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
            search_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def cart_button_click(self):
        """
        Clicks the cart button to view the items in the cart.
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.CART_BUTTON)))
        try:
            cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
            cart_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def login_button_click(self):
        """
        Clicks the login button to navigate to the login page.
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.LOGIN_BUTTON)))
        try:
            login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
            login_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def open_profile(self):
        """
        Opens the user profile dropdown and selects the profile option.
        """
        try:
            username_dropdown = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.USERNAME_DROPDOWN)))
            username_dropdown.click()
            profile_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.PROFILE_BUTTON)))
            profile_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def search_flow(self, item_name):
        """
        Performs the full search process: entering the item name and clicking the search button.
        Args:
            item_name (str): The name of the item to search for.
        """
        self.fill_search_input(item_name)
        self.search_button_click()

    def logout(self):
        """
        Logs out the user by clicking on the username dropdown and then clicking the logout button.
        """
        try:
            username_dropdown = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.USERNAME_DROPDOWN)))
            username_dropdown.click()
            logout_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGOUT_BUTTON)))
            logout_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

