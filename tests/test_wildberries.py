# Блок импортов
from selenium.webdriver.common.by import By


def test_open_first_card(driver):
    """ТК_001: Открытие первой карточки товара"""
    # Шаг 1: Открыть главную страницу
    driver.get('https://www.wildberries.ru/')

    # Шаг 2: Найти первую карточку товара
    first_card = driver.find_element(By.XPATH, '//article[@data-nm-id][1]')

    # Шаг 3: Кликнуть на карточку
    first_card.click()

    # Шаг 4: Проверить переход на страницу товара
    assert "detail" in driver.current_url

    # Шаг 5: Получить название товара
    title = driver.find_element(By.TAG_NAME, 'h1')
# Комментарий
    print(f"Товар '{title.text}' успешно открыт")

