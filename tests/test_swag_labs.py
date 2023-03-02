from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


USERNAME_LIST = ["standard_user",
                 "locked_out_user",
                 "problem_user",
                 "performance_glitch_user",
                 ]

PASSWORD = "secret_sauce"

URL = r"https://www.saucedemo.com/"


def test_login_user_and_add_last_product_to_cart(browser):
    """ User should be authenticated firstly then last product of products list should be added to cart """

    username = USERNAME_LIST[0]
    password = PASSWORD
    page = LoginPage(browser, URL)
    page.open()

    # login and verify user authentication
    page.make_login(username, password)

    products_page = ProductsPage(browser, browser.current_url)

    # adding the last product to cart and verify changes at button text
    products_page.add_the_last_product_to_cart()
    name = products_page.get_name_of_the_last_product()

    # going to cart for verify that the product had been added to the cart
    cart_page = CartPage(browser, browser.current_url)
    cart_page.go_to_cart_page()
    cart_page.verify_name_of_the_added_product(name)









