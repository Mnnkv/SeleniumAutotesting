from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        elements = browser.find_elements(By.CSS_SELECTOR, ":required")
        for element in elements:
            element.send_keys("Мой ответ")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        message = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(message, "Congratulations! You have successfully registered!", "Registration is not completed! Error")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        my_answer = "Buba"
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys(my_answer)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys(my_answer)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys(my_answer)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]').send_keys(my_answer)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]').send_keys(my_answer)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        message = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(message, "Congratulations! You have successfully registered!", "Registration is not completed! Error")


if __name__ == "__main__":
    unittest.main()
