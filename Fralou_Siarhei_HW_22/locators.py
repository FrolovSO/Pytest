from selenium import webdriver
from selenium.webdriver.common.by import By


def test_baraholka_onliner():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(10)
    url = 'https://baraholka.onliner.by'
    chrome.get(url=url)
    chrome.maximize_window()

    # Поиска конопки "Разместить объявление" "[class="b-fleamarket-button"]>a>span>strong"

    place_an_ad = chrome.find_element(By.CSS_SELECTOR, "[class='b-fleamarket-button']>a>span>strong")

    # Найти сколько объявлений в разделе "Ноутбуки. Компьютеры. Apple. Оргтехника", категория "Видеокарты"

    video_cards = chrome.find_element(By.XPATH,
                                      "//*[@class='cm-onecat'][2]/ul/li/a[starts-with(@href, './viewforum.php?f=286')]/../sup")

    # Найти сколько объявлений в разделе "Женская одежда", категория "Платья"

    dresses = chrome.find_element(By.XPATH,
                                  "//*[@class='cm-onecat'][2]/ul/li/a[starts-with(@href, './viewforum.php?f=255')]/../sup")

    print("Видеокарты: ", video_cards.text, "Платья: ", dresses.text)

    assert place_an_ad.text == ("Разместить объявление")

    chrome.close()
