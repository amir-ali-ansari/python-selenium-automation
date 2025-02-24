from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.application import Application
from pages.base_page import Page
from pages.amazon_sign_in_page import SignInPage
from pages.amazon_cart_page import CartPage
def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    # context.driver.implicitly_wait(4)
    context.wait=WebDriverWait(context, 10)
    # wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)
    context.pages = Page(context.driver)
    context.pages = SignInPage(context.driver)
    context.pages = CartPage(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
