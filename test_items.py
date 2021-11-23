from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


def test_button_existance(driver):
    driver.get(link)
    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form button')))
    print('Нашёл!')
