from behave import  given, then, when
from pages.main_page import MainPage
from app.application import Application
from pages.amazon_cart_page import CartPage
from time import sleep
from selenium.webdriver.common.by import By

SEARCH_BOX=(By.ID, "twotabsearchtextbox")
SEARCH_BTN=(By.ID, "nav-search-submit-button")
ITEM=(By.XPATH, "//div[@cel_widget_id='MAIN-SEARCH_RESULTS-3']")
ADD_CART = (By.ID, "add-to-cart-button")
CART_TEXT = (By.CSS_SELECTOR, ".a-size-medium-plus a-color-base sw-atc-text a-text-bold")


@when('search for item')
def search_for_item(context):
    context.app.base_page.input_text('okley flak', *SEARCH_BOX)
    context.app.base_page.click(*SEARCH_BTN)


@when('select Item')
def select_item(context):
    context.app.base_page.click(*ITEM)


@when('add to the cart')
def add_to_cart(context):
    context.app.base_page.click(*ADD_CART)
    sleep(5)



@then('verify there is one item')
def verify_add_to_cart(context):
    context.app.amazon_cart_page.item_in_cart()