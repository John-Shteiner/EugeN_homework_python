import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка драйвера (для Chrome)
driver = webdriver.Chrome()

try:
    # 1. Перейти на страницу
    url = "http://uitestingplayground.com/dynamicid"
    driver.get(url)
    print(f"Перешли на страницу: {url}")

    # Небольшая пауза, чтобы страница гарантированно загрузилась
    time.sleep(1)

    # 2. Найти синюю кнопку и кликнуть на неё
    # Используем надёжный селектор: текст кнопки и её класс
    # Это позволит избежать проблем с динамическим ID
    button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Button with Dynamic ID']")
    button.click()
    print("Кнопка успешно найдена и нажата!")

    # Небольшая пауза, чтобы визуально увидеть клик
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
    print("Браузер закрыт.")