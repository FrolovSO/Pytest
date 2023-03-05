from Fralou_Siarhei_HM_24.home_work_24.screens.automationpractice_home_screen import AutomationpracticeHomeScreen
from Fralou_Siarhei_HM_24.home_work_24.screens.automationpractice_shopping_cart_screen import \
    AutomationpracticeShoppingCartScreen
from Fralou_Siarhei_HM_24.home_work_24.screens.test_automationpractice_login_screen import AutomationpracticeLoginScreen


def test_automationpractice_home_steps(get_driver):
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)
    automationpracticeShoppingCartScreen = AutomationpracticeShoppingCartScreen(get_driver)
    automationpracticeLoginScreen = AutomationpracticeLoginScreen(get_driver)
    #####
    automationpracticeHome.open()
    automationpracticeHome.check_home_page_element()
    # - при переходе с главной страницы на страницу корзины и проверка на то, что корзина пуста.
    automationpracticeHome.navigate_to_cart()
    automationpracticeShoppingCartScreen.check_shopping_cart()
    automationpracticeShoppingCartScreen.check_cart_is_empty()
    automationpracticeShoppingCartScreen.navigate_to_home()
    automationpracticeHome.check_home_page_element()
    # - при переходе с главной страницы на страницу логина и проверка на то, что мы на странице логина.
    automationpracticeHome.navigate_to_login()
    automationpracticeLoginScreen.check_login_logo()
    automationpracticeLoginScreen.navigate_to_home()
    automationpracticeHome.check_home_page_element()


def test_automationpractice_shopping_cart(get_driver):
    automationpracticeShoppingCartScreen = AutomationpracticeShoppingCartScreen(get_driver)
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)
    #####
    automationpracticeShoppingCartScreen.open()
    automationpracticeShoppingCartScreen.check_shopping_cart()
    automationpracticeShoppingCartScreen.navigate_to_home()
    automationpracticeHome.check_home_page_element()


def test_automationpractice_login(get_driver):
    automationpracticeLoginScreen = AutomationpracticeLoginScreen(get_driver)
    automationpracticeHome = AutomationpracticeHomeScreen(get_driver)
    #####
    automationpracticeLoginScreen.open()
    automationpracticeLoginScreen.check_login_logo()
    automationpracticeLoginScreen.navigate_to_home()
    automationpracticeHome.check_home_page_element()
    automationpracticeHome.navigate_to_login()
    automationpracticeLoginScreen.check_login_logo()
