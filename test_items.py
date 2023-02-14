import time

import pytest
from selenium.webdriver.common.by import By


class TestItems:

    def test_checkout(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        add_cart = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert add_cart is not None, "No Such Element!"
        time.sleep(5)
