from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    def verify_name_of_the_added_product(self, name):
        """ Compares given name of the last product with names of products in cart """
        added_last_product = self.is_element_present(By.XPATH, f"//*[@class='cart_item']/div[2]/a/div[text()='{name}']")
        assert added_last_product, f"Product with name: {name} didn't add to the cart "
