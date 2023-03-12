from behave import *
from pytest_bdd import *

from Fralou_Siarhei_HM_24.home_work_24.screens.automationpractice_home_screen import AutomationpracticeHomeScreen
from Fralou_Siarhei_HM_24.home_work_24.screens.automationpractice_shopping_cart_screen import \
    AutomationpracticeShoppingCartScreen
from Fralou_Siarhei_HM_24.home_work_24.screens.test_automationpractice_login_screen import AutomationpracticeLoginScreen

scenarios('../features/web_shopping.feature')


@given('The Automation Practice Home page is displayed')
def open_automation_practice(get_driver):
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)

    automationpracticeHome.open()
    automationpracticeHome.check_home_page_element()


@when('Navigate from Home to Shopping Cart page')
def navigate_to_shopping_car(get_driver):
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)
    automationpracticeShoppingCartScreen = AutomationpracticeShoppingCartScreen(get_driver)

    automationpracticeHome.navigate_to_cart()
    automationpracticeShoppingCartScreen.check_shopping_cart()


@then('Accept we on the  Shopping Cart page and Cart is empty')
def accept_cart_is_empty(get_driver):
    automationpracticeShoppingCartScreen = AutomationpracticeShoppingCartScreen(get_driver)

    automationpracticeShoppingCartScreen.check_shopping_cart()
    automationpracticeShoppingCartScreen.check_cart_is_empty()


@when('Navigate from Shopping Cart to Home page')
def navigate_to_home_from_cart(get_driver):
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)
    automationpracticeShoppingCartScreen = AutomationpracticeShoppingCartScreen(get_driver)

    automationpracticeShoppingCartScreen.navigate_to_home()
    automationpracticeHome.check_home_page_element()


@then('Navigate from Home to Login page and assrt login element')
def navigate_and_assert_login_page(get_driver):
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)
    automationpracticeLoginScreen = AutomationpracticeLoginScreen(get_driver)

    automationpracticeHome.navigate_to_login()
    automationpracticeLoginScreen.check_login_logo()
