from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    #проскроллим страницу до первого input
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.TAG_NAME, "input"))
    #вводим все значения и заполняем чек-бокс, радио, нажимаем сабмит
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(5)
    browser.quit()