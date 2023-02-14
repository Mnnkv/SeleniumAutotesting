import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for el in elements[:3]:
        el.send_keys("Hello")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'recap.txt')
    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    time.sleep(5)
    browser.quit()


