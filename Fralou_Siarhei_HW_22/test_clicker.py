from selenium import webdriver
from selenium.webdriver.common.by import By


def test_clicker_1():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/complicated-page'
    chrome.get(url=url)
    # chrome.maximize_window()
    # Нажмите на 2-ю сверху кнопку во втором столбце используя:
    # XPATH

    xpath_button = chrome.find_element(By.XPATH,
                                       "//*[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light']")

    xpath_button.click()

    chrome.close()


def test_clicker_2():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/complicated-page'
    chrome.get(url=url)
    chrome.maximize_window()
    # Нажмите на 2-ю сверху кнопку во втором столбце используя:
    # CSS

    css_button = chrome.find_element(By.CSS_SELECTOR,
                                     "div.et_pb_button_module_wrapper.et_pb_button_4_wrapper.et_pb_button_alignment_left.et_pb_module > a")

    css_button.click()
    chrome.close()


def test_clicker_3():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://ultimateqa.com/complicated-page'
    chrome.get(url=url)
    chrome.maximize_window()
    # Нажмите на 2-ю сверху кнопку во втором столбце используя:
    # class_name

    class_name_button = chrome.find_element(By.CLASS_NAME, "et_pb_button_4")

    class_name_button.click()

    chrome.close()
