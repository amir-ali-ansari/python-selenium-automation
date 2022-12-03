from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_TEXT = (By.XPATH,'//div[@class="a-row sc-your-amazon-cart-is-empty"]' )
    CART_NUMBER = (By.ID, "nav-cart-count")

    def cart_is_empty(self):
        expected_value = 'Your Amazon Cart is empty'
        actual_value = self.driver.find_element(*self.CART_TEXT).text
        assert expected_value == actual_value, f'error| Expected{expected_value}, but got {actual_value}'


    def item_in_cart(self):
        expected_number = '1'
        actual_number = self.driver.find_element(*self.CART_NUMBER).text
        assert expected_number == actual_number , f'Expected{expected_number} but it shows {actual_number}'