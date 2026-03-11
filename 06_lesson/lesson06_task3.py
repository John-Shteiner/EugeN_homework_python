from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(url)
    print(f"✅ Перешли на страницу: {url}")
    
    
    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )
    print("✅ Все картинки загружены")
    
    
    images = driver.find_elements(By.TAG_NAME, "img")
    
    
    if len(images) >= 3:
        third_image = images[2]
        src_attribute = third_image.get_attribute("src")
        
        print(f"\n--- Атрибут src 3-й картинки ---")
        print(src_attribute)
        print("---------------------------------\n")
    else:
        print("❌ На странице меньше 3-х картинок")
    
finally:
    driver.quit()
    print("✅ Браузер закрыт")