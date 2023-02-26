from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web():
    chrome = webdriver.Chrome('./chromedriver.exe')
    url = 'https://google.com'
    chrome.get(url=url)
    #chrome.maximize_window()
    accept_button = chrome.find_element(By.XPATH, "//*[@id='W0wltc']/div")
    accept_button.click()
    search_box = chrome.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    search_box.send_keys('python 3.10')
    search_box.submit()
    search_element = chrome.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div[1]/div/a/h3")
    assert search_element.is_displayed()
    chrome.close()
