from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def make_login(self, username, password):
        """ Authenticates user and asserts login process"""
        username_field = self.browser.find_element(By.ID, "user-name").send_keys(username)
        password_field = self.browser.find_element(By.ID, "password").send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()
        assert self.browser.find_element(By.ID, "logout_sidebar_link"), f"User is not authenticated"