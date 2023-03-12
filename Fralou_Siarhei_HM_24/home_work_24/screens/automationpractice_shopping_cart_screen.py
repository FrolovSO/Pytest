from selenium import webdriver
from selenium.webdriver.common.by import By

from Fralou_Siarhei_HM_24.home_work_24.control.base_page_demo import BasePage


class AutomationpracticeShoppingCartHomeLocators:
    your_shopping_cart_locator = (By.CSS_SELECTOR, '[id="center_column"] > [class="page-heading"]')
    return_to_home_locator = (By.XPATH, '//*[@id="columns"]/div/a')
    empty_cart_locator = (By.XPATH, '//*[@class="alert alert-warning"]')

class AutomationpracticeShoppingCartScreen(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php'

    def check_shopping_cart(self):
        assert self.find_element(AutomationpracticeShoppingCartHomeLocators.your_shopping_cart_locator).is_displayed()
        assert self.url in self.webdriver.current_url

    def check_cart_is_empty(self):
        cart_is_empty = self.find_element(AutomationpracticeShoppingCartHomeLocators.empty_cart_locator).text
        assert cart_is_empty == 'Your shopping cart is empty.'

    def navigate_to_home(self):
        self.click_element(AutomationpracticeShoppingCartHomeLocators.return_to_home_locator)
