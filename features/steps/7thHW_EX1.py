from behave import  given, then, when
from pages.main_page import MainPage
from app.application import Application
from pages.amazon_cart_page import CartPage
from selenium.webdriver.common.by import By

ORDER_BTN = (By.ID, "nav-orders")
CART_ICON = (By.XPATH, "//span[@class= 'nav-cart-icon nav-sprite']")


@given("open Amazon")
def open_amazon(context):
    context.app.main_page.open_main()


@when("click on Amazon orders")
def click_on_orders(context):
    context.app.base_page.click(*ORDER_BTN)


@then("Verify sign in page is open")
def verify_sign_in_page_shown(context):
    context.app.sign_in_page.sign_in_appeared()


@when("Click on cart")
def Click_on_cart (context):
    context.app.base_page.click(*CART_ICON)


@then("Verity cart is empty")
def verify_cart_is_empty(context):
    context.app.amazon_cart_page.cart_is_empty()