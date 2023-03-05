from selenium import webdriver
from selenium.webdriver.common.by import By

from Fralou_Siarhei_HM_24.home_work_24.control.base_page_demo import BasePage


class AutomationpracticeLoginLocators:
    login_title_locator = (By.CSS_SELECTOR, '[id="center_column"] > [class="page-heading"]')
    return_to_home_locator = (By.XPATH, '//*[@id="columns"]/div/a')


class AutomationpracticeLoginScreen(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'http://automationpractice.pl/index.php?controller=authentication&back=my-account'

    def check_login_logo(self):
        assert self.find_element(AutomationpracticeLoginLocators.login_title_locator).is_displayed()

    def navigate_to_home(self):
        self.click_element(AutomationpracticeLoginLocators.return_to_home_locator)
