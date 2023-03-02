import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    def add_the_last_product_to_cart(self):

        """ adds the last product to cart"""
        last_product = len(self.browser.find_elements(By.CLASS_NAME, "inventory_item"))
        self.browser.find_element(By.XPATH, f"//*[@id='inventory_container']/div/div[{last_product}]/div[2]/div[2]/button").click()
        remove_button = self.browser.find_element(By.XPATH, f"//*[@id='inventory_container']/div/div[{last_product}]/div[2]/div[2]/button")
        assert remove_button.text == "Remove", F"Button 'Add to cart' doesn't work"

    def get_name_of_the_last_product(self):

        """ return name of the last product """
        last_product = len(self.browser.find_elements(By.CLASS_NAME, "inventory_item"))
        name = self.browser.find_element(By.XPATH, f"//*[@id='inventory_container']/div/div[{last_product}]/div[2]/div/a/div").text
        print(name)
        return name



