import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


driver = webdriver.Firefox()

try:
    
    url = "http://the-internet.herokuapp.com/inputs"
    driver.get(url)
    print(f"✅ Перешли на страницу: {url}")
    
    
    time.sleep(1)
    
    
    input_field = driver.find_element(By.TAG_NAME, "input")
    print("✅ Поле ввода найдено")
    
    
    input_field.send_keys("12345")
    print("✅ Ввели текст: 12345")
    time.sleep(1)  
    
    input_field.clear()
    print("✅ Поле очищено")
    time.sleep(1)  
    
    
    input_field.send_keys("54321")
    print("✅ Ввели текст: 54321")
    time.sleep(2)  
    
finally:
    
    driver.quit()
    print("✅ Браузер закрыт")