import time
from selenium.webdriver.support.ui import Select
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage
from infra.utils import Utils
from logic.browser.base_app_page import BaseAppPage


class OrderPage(BasePage):
    IFRAME = '//iframe[@allowtransparency="true"]'
    CREDIT_CARD_BUTTON = '//div[@aria-label="Debit or Credit Card"]'
    CARD_NUMBER = '//input[@id="credit-card-number"]'
    CARD_DATE = '//input[@id="expiry-date"]'
    CARD_CVV = '//input[@id="credit-card-security"]'
    COSTUMER_NAME = '//input[@id="billingAddress.givenName"]'
    COSTUMER_FAMILY = '//input[@id="billingAddress.familyName"]'
    COSTUMER_STREET = '//input[@id="billingAddress.line1"]'
    COSTUMER_CITY = '//input[@id="billingAddress.city"]'
    STATE_SELECT = '//select[@id="billingAddress.state"]'
    COSTUMER_ZIPCODE = '//input[@id="billingAddress.postcode"]'
    COSTUMER_PHONE = '//input[@id="phone"]'
    COSTUMER_EMAIL = '//input[@id="email"]'
    PAY_NOW_BUTTON = '//button[@id="submit-button"]'
    PAID_ALERT = '//div[@class="fade alert alert-success show"]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def switch_to_iframe(self):
        # Wait for the iframe to be present and switch to it
        iframe_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.IFRAME)))
        self._driver.switch_to.frame(iframe_element)

    def click_credit_card_button(self):
        self.switch_to_iframe()
        credit_card_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CREDIT_CARD_BUTTON)))
        credit_card_button.click()

    def enter_card_number(self, card_number):
        self.switch_to_iframe()
        credit_card_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_NUMBER)))
        credit_card_button.clear()
        credit_card_button.send_keys(card_number)

    def enter_card_date(self, card_date):
        card_date_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_DATE)))
        card_date_input.clear()
        card_date_input.send_keys(card_date)

    def enter_card_cvv(self, card_cvv):
        card_cvv_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_CVV)))
        card_cvv_input.clear()
        card_cvv_input.send_keys(card_cvv)

    def enter_customer_firstname(self, firstname):
        customer_name_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_NAME)))
        customer_name_input.clear()
        customer_name_input.send_keys(firstname)

    def enter_customer_lastname(self, lastname):
        customer_family_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_FAMILY)))
        customer_family_input.clear()
        customer_family_input.send_keys(lastname)

    def enter_customer_street(self, street):
        customer_street_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_STREET)))
        customer_street_input.clear()
        customer_street_input.send_keys(street)

    def enter_customer_city(self, city):
        customer_city_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_CITY)))
        customer_city_input.clear()
        customer_city_input.send_keys(city)

    def enter_customer_zipcode(self, zipcode):
        customer_zipcode_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_ZIPCODE)))
        customer_zipcode_input.clear()
        customer_zipcode_input.send_keys(zipcode)

    def enter_customer_phone(self, phone):
        customer_phone_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_PHONE)))
        customer_phone_input.clear()
        customer_phone_input.send_keys(phone)

    def enter_customer_email(self, email):
        customer_email_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_EMAIL)))
        customer_email_input.clear()
        customer_email_input.send_keys(email)

    def pick_state(self):
        select_state = Select(WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.STATE_SELECT))))
        select_state.select_by_value("NY")

    def click_pay_now_button(self):
        pay_now_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PAY_NOW_BUTTON)))
        time.sleep(3)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", pay_now_button)
        pay_now_button.click()

    def payment_flow(self, card_number, date, cvv, firstname, lastname, street_name, city, zipcode, phone, email):
        self.enter_card_number(card_number)
        self.enter_card_date(date)
        self.enter_card_cvv(cvv)
        self.pick_state()
        self.enter_customer_firstname(firstname)
        self.enter_customer_lastname(lastname)
        self.enter_customer_street(street_name)
        self.enter_customer_city(city)
        self.enter_customer_zipcode(zipcode)
        self.enter_customer_phone(phone)
        self.enter_customer_email(email)
        self.click_pay_now_button()
