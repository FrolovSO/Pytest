import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_submit_1():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/complicated-page'
    chrome.get(url=url)
    chrome.maximize_window()

    name = "Test"
    address = "Test@test.test"
    message_text = "My test message"

    # Заполните форму обратной связи
    input_name = chrome.find_element(By.CSS_SELECTOR, "#et_pb_contact_name_0")
    email_address = chrome.find_element(By.CSS_SELECTOR, "#et_pb_contact_email_0")
    message = chrome.find_element(By.CSS_SELECTOR, "#et_pb_contact_message_0")
    input_name.send_keys(name)
    email_address.send_keys(address)
    message.send_keys(message_text)

    # Нажмите на кнопку "Submit"
    submit_button = chrome.find_element(By.CSS_SELECTOR, ".et_contact_bottom_container > button")
    captcha_question = chrome.find_element(By.CSS_SELECTOR, ".et_contact_bottom_container > div > p >span")
    captcha_question_input = chrome.find_element(By.CSS_SELECTOR, ".et_contact_bottom_container > div > p > input")
    captcha_question.text
    captcha_value = captcha_question.text.split(' + ')
    captcha_answer = (int(captcha_value[0]) + int(captcha_value[-1]))
    captcha_question_input.send_keys(captcha_answer)
    time.sleep(2)
    submit_button.click()
    # Проверьте наличие сообщения "Form filled out successfully"
    time.sleep(2)
    success_message = chrome.find_element(By.CSS_SELECTOR, ".et-pb-contact-message > p")
    assert success_message.text == "Thanks for contacting us"

    chrome.close()


def test_submit_2():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/complicated-page'
    chrome.get(url=url)
    chrome.maximize_window()
    name = "Chamar"
    # Заполните поле "Name"
    user_name_input = chrome.find_element(By.CSS_SELECTOR, "[action='https://ultimateqa.com/backoffice'] > p > input")
    user_name_input.send_keys(name)
    # Нажмите на кнопку "Submit"
    login_button = chrome.find_element(By.CSS_SELECTOR,
                                       "[action='https://ultimateqa.com/backoffice'] > p:nth-of-type(4) > button")
    login_button.click()
    # Проверьте наличие сообщения об ошибке
    error_locator = chrome.find_element(By.CSS_SELECTOR, "#login_error")
    assert error_locator.text == ("Error: The password field is empty.")

    chrome.close()


def test_submit_3():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/complicated-page'
    chrome.get(url=url)
    chrome.maximize_window()
    # Заполните поле "Message"
    message_input = chrome.find_element(By.CSS_SELECTOR,
                                        ".et_pb_contact_form_1 [action='https://ultimateqa.com/complicated-page/'] #et_pb_contact_message_1")
    message_input.send_keys("Test test")
    # Нажмите на кнопку "Submit"
    submit_button = chrome.find_element(By.CSS_SELECTOR,
                                        ".et_pb_contact_form_1 [action='https://ultimateqa.com/complicated-page/'] button")
    submit_button.click()
    # Проверьте наличие сообщения об ошибке
    time.sleep(2)
    error_message = chrome.find_element(By.CSS_SELECTOR, "#et_pb_contact_form_1 .et-pb-contact-message > p")
    assert error_message.text == ("Make sure you fill in all required fields.")

    chrome.close()
