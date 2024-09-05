from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
#time.sleep(5)

driver.get("http://suninjuly.github.io/find_xpath_form")

try:
    input_name = driver.find_element(By.XPATH, '//input[@name="first_name"]')
    input_name.send_keys("Irina")
    input_l_name = driver.find_element(By.XPATH, '//input[@name="last_name"]')
    input_l_name.send_keys("Bannikova")
    input_city = driver.find_element(By.XPATH, '//input[@class="form-control city"]')
    input_city.send_keys("Moscow")
    input_city = driver.find_element(By.XPATH, '//input[@id="country"]')
    input_city.send_keys("Russia")
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    
finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        driver.close()
        driver.quit()
    
       # не забываем оставить пустую строку в конце файла
    





