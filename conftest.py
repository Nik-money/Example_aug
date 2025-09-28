import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    """Запускает браузер с установленными настройками"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture()
def close_cookies_banner(driver):
    """Закрывает баннер куки перед каждым тестом"""

    cookie_btn = driver.find_element(By.CSS_SELECTOR, 'div.cookies button')
    cookie_btn.click()
