from selenium import webdriver
from selenium.webdriver.common.by import By

from Fralou_Siarhei_HM_24.home_work_24.control.base_page_demo import BasePage


class PotterPageLocators:
    #iframe[id="iframeResult"]
    iframe_locator = (By.CSS_SELECTOR, '[id="iframeResult"]')
    button_locator = (By.CSS_SELECTOR, 'button[onclick="myFunction()"]')
    success_message_locator = (By.CSS_SELECTOR, 'p#demo')


class PotterPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.url = 'https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt'

    def click_try_it(self):
        self.switch_to_default_context()
        self.switch_to_iframe(PotterPageLocators.iframe_locator)
        self.click_element(PotterPageLocators.button_locator)

    def fill_name(self, name):
        self.fill_and_accept_alert(name)

    #
    # def click_run_button(self):
    #     self.switch_to_default_context()

    def verify_message(self, name):
        self.switch_to_default_context()
        self.switch_to_iframe(PotterPageLocators.iframe_locator)
        message = self.get_text_from_element(PotterPageLocators.success_message_locator)
        assert message == f'Hello {name}! How are you today?'