import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser.base_page import BasePage


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
    PAID_ALERT = '//div[contains(text(),"Paid on")]'

    def __init__(self, driver):
        """
            Initializes an instance of BaseAppPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def switch_to_iframe(self):
        """
        Switches to the iframe containing the payment form.
        """
        # Wait for the iframe to be present and switch to it
        iframe_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.IFRAME)))
        self._driver.switch_to.frame(iframe_element)

    def click_credit_card_button(self):
        """
        Clicks the credit card payment button after switching to the iframe.
        """
        self.switch_to_iframe()
        credit_card_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CREDIT_CARD_BUTTON)))
        credit_card_button.click()

    def enter_card_number(self, card_number):
        """
        Enters the credit card number in the payment form.
        Args:
            card_number (str): The credit card number.
        """
        self.switch_to_iframe()
        credit_card_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_NUMBER)))
        credit_card_button.clear()
        credit_card_button.send_keys(card_number)

    def enter_card_date(self, card_date):
        """
        Enters the card expiration date in the payment form.
        Args:
            card_date (str): The card expiration date.
        """
        card_date_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_DATE)))
        card_date_input.clear()
        card_date_input.send_keys(card_date)

    def enter_card_cvv(self, card_cvv):
        """
        Enters the card CVV number in the payment form.
        Args:
            card_cvv (str): The card CVV number.
        """
        card_cvv_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CARD_CVV)))
        card_cvv_input.clear()
        card_cvv_input.send_keys(card_cvv)

    def enter_customer_firstname(self, firstname):
        """
        Enters the customer's first name in the payment form.
        Args:
            firstname (str): The customer's first name.
        """
        customer_name_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_NAME)))
        customer_name_input.clear()
        customer_name_input.send_keys(firstname)

    def enter_customer_lastname(self, lastname):
        """
        Enters the customer's last name in the payment form.
        Args:
            lastname (str): The customer's last name.
        """
        customer_family_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_FAMILY)))
        customer_family_input.clear()
        customer_family_input.send_keys(lastname)

    def enter_customer_street(self, street):
        """
        Enters the customer's street address in the payment form.
        Args:
            street (str): The customer's street address.
        """
        customer_street_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_STREET)))
        customer_street_input.clear()
        customer_street_input.send_keys(street)

    def enter_customer_city(self, city):
        """
        Enters the customer's city in the payment form.
        Args:
            city (str): The customer's city.
        """
        customer_city_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_CITY)))
        customer_city_input.clear()
        customer_city_input.send_keys(city)

    def enter_customer_zipcode(self, zipcode):
        """
        Enters the customer's zipcode in the payment form.
        Args:
            zipcode (str): The customer's zipcode.
        """
        customer_zipcode_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_ZIPCODE)))
        customer_zipcode_input.clear()
        customer_zipcode_input.send_keys(zipcode)

    def enter_customer_phone(self, phone):
        """
        Enters the customer's phone number in the payment form.
        Args:
            phone (str): The customer's phone number.
        """
        customer_phone_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_PHONE)))
        customer_phone_input.clear()
        customer_phone_input.send_keys(phone)

    def enter_customer_email(self, email):
        """
        Enters the customer's email address in the payment form.
        Args:
            email (str): The customer's email address.
        """
        customer_email_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.COSTUMER_EMAIL)))
        customer_email_input.clear()
        customer_email_input.send_keys(email)

    def pick_state(self):
        """
        Selects the state from the dropdown menu.
        """
        select_state = Select(WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.STATE_SELECT))))
        select_state.select_by_value("NY")

    def click_pay_now_button(self):
        """
        Clicks the "Pay Now" button to complete the payment.
        """
        pay_now_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PAY_NOW_BUTTON)))
        time.sleep(3)
        self._driver.execute_script("arguments[0].scrollIntoView(true);", pay_now_button)
        time.sleep(1)
        pay_now_button.click()

    def payment_flow(self, payment_details):
        """
         Completes the payment form with the provided details and submits the payment.
        """
        self.enter_card_number(payment_details['Credit_Card_Number'])
        self.enter_card_date(payment_details['Expiry_Date'])
        self.enter_card_cvv(payment_details['cvv'])
        self.pick_state()
        self.enter_customer_firstname(payment_details['First_Name'])
        self.enter_customer_lastname(payment_details['Last_Name'])
        self.enter_customer_street(payment_details['street'])
        self.enter_customer_city(payment_details['city'])
        self.enter_customer_zipcode(payment_details['zipcode'])
        self.enter_customer_phone(payment_details['Phone'])
        self.enter_customer_email(payment_details['email'])
        self.click_pay_now_button()
        self._driver.switch_to.default_content()
