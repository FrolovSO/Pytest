from selenium import webdriver
from selenium.webdriver.common.by import By

from Fralou_Siarhei_HM_24.home_work_24.control.base_page_demo import BasePage


class AutomationpracticeHomeLocators:

    my_store_slider_row_locator = (By.CSS_SELECTOR, '[id="slider_row"]')

    navigate_to_cart_locator = (By.XPATH, '//*[@class="shopping_cart"]/a')

    navigate_to_login_locator = (By.XPATH, '//*[@class="header_user_info"]/a')


class AutomationpracticeHomeScreen(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php'

    def check_home_page_element(self):
        assert self.find_element(AutomationpracticeHomeLocators.my_store_slider_row_locator).is_displayed()

    def navigate_to_cart(self):
        self.click_element(AutomationpracticeHomeLocators.navigate_to_cart_locator)

    def navigate_to_login(self):
        self.click_element(AutomationpracticeHomeLocators.navigate_to_login_locator)
