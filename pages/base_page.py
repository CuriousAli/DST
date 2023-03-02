from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ Open url"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """ Check availability of the element at page"""
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_cart_page(self):
        """ Redirecting to cart page via cart icon at header """
        self.browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
