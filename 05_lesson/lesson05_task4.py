import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера Firefox
driver = webdriver.Firefox()

try:
    # 1. Перейти на страницу логина
    url = "http://the-internet.herokuapp.com/login"
    driver.get(url)
    print(f"✅ Перешли на страницу: {url}")
    
    # Явное ожидание загрузки страницы (появления формы логина)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    
    # 2. Найти поле username и ввести значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("✅ Введено имя пользователя: tomsmith")
    
    # 3. Найти поле password и ввести значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("✅ Введен пароль")
    
    # 4. Найти кнопку Login и нажать её
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("✅ Нажата кнопка Login")
    
    # Небольшая пауза для обработки входа и появления плашки
    time.sleep(1)
    
    # 5. Найти зеленую плашку с сообщением об успехе и вывести её текст
    # Плашка имеет класс 'flash success'
    success_message = driver.find_element(By.CLASS_NAME, "flash.success")
    message_text = success_message.text
    print("\n--- Текст зеленой плашки ---")
    print(message_text)
    print("-----------------------------\n")
    
    # Пауза, чтобы визуально увидеть результат
    time.sleep(2)
    
finally:
    # 6. Закрыть браузер
    driver.quit()
    print("✅ Браузер закрыт")