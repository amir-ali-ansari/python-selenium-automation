from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):

    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def sign_in_appeared(self):
        expected_value = 'Sign in'
        actual_value = self.driver.find_element(*self.SIGN_IN_TEXT).text
        assert expected_value == actual_value, f'error| Expected{expected_value}, but got {actual_value}'