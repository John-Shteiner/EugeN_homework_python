from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    
    url = "http://uitestingplayground.com/textinput"
    driver.get(url)
    print(f"✅ Перешли на страницу: {url}")
    
    
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#newButtonName"))
    )
    input_field.send_keys("SkyPro")
    print("✅ Ввели текст 'SkyPro' в поле ввода")
    
    
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    print("✅ Нажали на синюю кнопку")
    
    
    
    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )
    
    button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(f"\n--- Текст кнопки после нажатия ---")
    print(button_text)
    print("---------------------------------\n")
    
finally:
    driver.quit()
    print("✅ Браузер закрыт")