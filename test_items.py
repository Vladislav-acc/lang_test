from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button_existance(driver):
    driver.get(link)
    driver.implicitly_wait(5)
    button = driver.find_elements_by_css_selector('#add_to_basket_form button')
    assert button, 'Кнопка "Добавить в корзину" не найдена!'
