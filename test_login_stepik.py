import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPage:

    ufo_links = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
    ]

    @pytest.mark.parametrize('links', ufo_links)
    def test_login(self, browser, links):
        browser.get(links)
        browser.implicitly_wait(15)

        browser.find_element(By.ID, "ember33").click()
        browser.find_element(By.ID, "id_login_email").send_keys("mnnkov@gmail.com")
        browser.find_element(By.ID, "id_login_password").send_keys("prwrY7q%v_gQ9/e")
        browser.find_element(By.CLASS_NAME, "button_with-loader").click()
        time.sleep(3)

        browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(math.log(int(time.time() - 0.4)))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
        feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        assert feedback == "Correct!", "Texts do not match!"
        browser.find_element(By.CLASS_NAME, "again-btn").click()










