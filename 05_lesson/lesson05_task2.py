import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    
    url = "http://uitestingplayground.com/dynamicid"
    driver.get(url)
    print(f"Перешли на страницу: {url}")

    
    time.sleep(1)

    
    button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Button with Dynamic ID']")
    button.click()
    print("Кнопка успешно найдена и нажата!")

    
    time.sleep(2)

finally:
    
    driver.quit()
    print("Браузер закрыт.")