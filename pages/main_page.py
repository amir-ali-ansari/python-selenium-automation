from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage (Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')

    def open_main(self):
        self.driver.get('https://www.amazon.com/')



    def search_product(self):
        self.input_text("coffee", *self.SEARCH_INPUT )
        self.click(*self.SEARCH_BTN)
