import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.yandex.ru/search/?text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD&lr=213"

def test_reverse_translation():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(3)
        word_left1 = "Дерево"
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Введите текст"]').send_keys(word_left1)
        time.sleep(4)
        word_right1 = browser.find_element(By.CLASS_NAME, "Translate-TargetText").text
        browser.find_element(By.CLASS_NAME, "Translate-ReverseButton").click()
        time.sleep(4)
        assert "Дерево" == browser.find_element(By.CLASS_NAME, "Translate-TargetText").text, "Перевод не сработал"
        assert word_right1 == browser.find_element(By., '').text, "Окно ввода текста забаговало"


    finally:
        time.sleep(3)
        browser.quit()