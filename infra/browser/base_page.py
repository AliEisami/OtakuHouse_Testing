from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        """
            Initializes an instance of BasePage with a WebDriver instance.
            Args:
                driver (WebDriver): The WebDriver instance used for interacting with the web browser.
        """
        self._driver = driver

    def scroll(self, scroll):
        self._driver.execute_script(f"window.scrollTo(0, {scroll})")
