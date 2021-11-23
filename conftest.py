import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: ru, en, is')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope='function')
def driver(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("Choose your browser wisely")
    yield driver
    driver.quit()
