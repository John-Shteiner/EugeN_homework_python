from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

try:
    
    driver.get("http://uitestingplayground.com/classattr")


    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    blue_button.click()

    
    alert = driver.switch_to.alert
    alert.accept()
    
    print("Кнопка успешно нажата, alert закрыт.")

finally:
    
    sleep(2)
    
    driver.quit()