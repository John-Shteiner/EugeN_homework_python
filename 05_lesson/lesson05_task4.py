import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

try:
    
    url = "http://the-internet.herokuapp.com/login"
    driver.get(url)
    print(f"✅ Перешли на страницу: {url}")
    

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    
    
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")
    print("✅ Введено имя пользователя: tomsmith")
    
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("✅ Введен пароль")
    
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("✅ Нажата кнопка Login")
    

    time.sleep(1)
    

    success_message = driver.find_element(By.CLASS_NAME, "flash.success")
    message_text = success_message.text
    print("\n--- Текст зеленой плашки ---")
    print(message_text)
    print("-----------------------------\n")
    
    
    time.sleep(2)
    
finally:
    
    driver.quit()
    print("✅ Браузер закрыт")