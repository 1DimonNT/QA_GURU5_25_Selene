import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def browser_management():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    browser.config.timeout = 10.0

    browser.config.window_width = 1600
    browser.config.window_height = 1200

    yield

    browser.quit()
