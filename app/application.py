from pages.main_page import MainPage
from pages.base_page import Page
from pages.amazon_sign_in_page import SignInPage
from pages.amazon_cart_page import CartPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.base_page = Page(self.driver)
        self.amazon_sign_in_page = SignInPage(self.driver)
        self.amazon_cart_page = CartPage(self.driver)
