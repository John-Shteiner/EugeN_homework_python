from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:
    
    url = "http://uitestingplayground.com/ajax"
    driver.get(url)
    print(f"✅ Перешли на страницу: {url}")
    
    
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxButton"))
    )
    button.click()
    print("✅ Нажали на синюю кнопку")
    
    
    
    success_message = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    
    
    message_text = success_message.text
    print(f"\n--- Текст зелёной плашки ---")
    print(message_text)
    print("-----------------------------\n")
    
finally:
    
    driver.quit()
    print("✅ Браузер закрыт")