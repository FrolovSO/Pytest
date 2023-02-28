from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_checkbox(get_driver):
    chrome = get_driver
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome.get(url)
    # Найти чекбокс
    check_box_locator = (By.CSS_SELECTOR, '[label="blah"]')
    check_box = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(check_box_locator))
    check_box.is_displayed()
    # Нажать на кнопку
    remove_button_locator = (By.CSS_SELECTOR, '[class="example"] #checkbox-example [type="button"]')
    remove_button = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(remove_button_locator))
    remove_button.click()
    # Дождаться надписи “It’s gone”
    alert_message_locator = (By.CSS_SELECTOR, '[class="example"] #checkbox-example #message')
    alert_message = WebDriverWait(chrome, 10).until(EC.presence_of_element_located(alert_message_locator))
    alert_message.is_displayed()
    # Проверить, что чекбокса нет
    check_box = WebDriverWait(chrome, 10).until_not(EC.presence_of_element_located(check_box_locator))
    assert check_box == True
    # Найти инпут
    input_field_lacator = (By.CSS_SELECTOR, '[class="example"] #input-example input')
    input_field = WebDriverWait(chrome, 10).until((EC.presence_of_element_located(input_field_lacator)))
    # input_field = chrome.find_element(By.CSS_SELECTOR, '').is_enabled()
    # Проверить, что он disabled
    assert input_field.is_enabled() == False
    # Нажать на кнопку
    enable_button = chrome.find_element(By.CSS_SELECTOR, '[class="example"] #input-example button')
    enable_button.click()
    # Дождаться надписи “It's enabled!”
    alert_message_enabled_locator = (By.CSS_SELECTOR, '[class="example"] #input-example #message')
    alert_message_enabled = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located(alert_message_enabled_locator))
    alert_message_enabled.is_displayed()
    # Проверить, что инпут enabled
    assert input_field.is_enabled()


def test_frames(get_driver):
    chrome = get_driver
    url = 'http://the-internet.herokuapp.com/iframe'
    chrome.get(url)
    # Открыть iFrame
    frame_locator = (By.CSS_SELECTOR, '#mce_0_ifr')
    WebDriverWait(chrome, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_locator))
    # Проверить, что текст внутри параграфа равен “Your content goes here.”
    frame_message_locator = (By.XPATH, '//*[@id="tinymce"]/p')
    frame_message = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located(frame_message_locator))
    frame_message.is_displayed()
    assert frame_message.text == 'Your content goes here.'

    chrome.switch_to.default_content()
    check_to_defalt_conten_element = chrome.find_element(By.CSS_SELECTOR, '.example h3')
    assert check_to_defalt_conten_element.text == 'An iFrame containing the TinyMCE WYSIWYG Editor'