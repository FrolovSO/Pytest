from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_first():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'http://thedemosite.co.uk/savedata.php'
    chrome.get(url=url)
    # chrome.maximize_window()
    username = chrome.find_element(By.XPATH, "//*[@name='username']")
    username.send_keys('admin')

    password = chrome.find_element(By.XPATH, "//*[@name='password']")
    password.send_keys('password')

    save = chrome.find_element(By.XPATH, "//*[@name='FormsButton2']")
    save.click()

    search_element = chrome.find_element(By.XPATH, "//*[@name='FormsButton2']")

    assert search_element.is_displayed()
    chrome.close()


def test_web_second():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://demoqa.com/text-box'
    chrome.get(url=url)
    # chrome.maximize_window()
    data_for_name = 'Admin Petrovich'
    data_for_email = 'APetrovich@admin.com'
    data_for_current_address = 'Geodezichckaya 9'
    data_for_permanent_address = 'Geodezichckaya 12'

    full_name = chrome.find_element(By.XPATH, "//input[@id='userName']")
    full_name.send_keys(data_for_name)

    email = chrome.find_element(By.XPATH, "//input[@id='userEmail']")
    email.send_keys(data_for_email)

    current_address = chrome.find_element(By.XPATH, "//textarea[@id='currentAddress']")
    current_address.send_keys(data_for_current_address)

    permanent_address = chrome.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
    permanent_address.send_keys(data_for_permanent_address)

    submit = chrome.find_element(By.CSS_SELECTOR, "#submit")
    submit.click()

    search_element = chrome.find_element(By.CSS_SELECTOR, "#output")

    text_name = chrome.find_element(By.CSS_SELECTOR, "#name")

    text_email = chrome.find_element(By.CSS_SELECTOR, "#email")

    text_current_address = chrome.find_element(By.CSS_SELECTOR, "#currentAddress:nth-of-type(3)")

    text_permanent_address = chrome.find_element(By.CSS_SELECTOR, "#permanentAddress:nth-of-type(4)")

    assert search_element.is_displayed()

    assert text_name.text == ("Name:" + data_for_name)

    assert text_email.text == ("Email:" + data_for_email)

    assert text_current_address.text == ("Current Address :" + data_for_current_address)

    assert text_permanent_address.text == ("Permananet Address :" + data_for_permanent_address)

    chrome.close()
