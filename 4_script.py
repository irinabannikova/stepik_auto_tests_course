from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()
#time.sleep(5)

driver.get("http://suninjuly.github.io/find_link_text")

link = driver.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

try:
    input_name = driver.find_element(By.CSS_SELECTOR, '.form-group [name="first_name"]')
    input_name.send_keys("Irina")
    input_l_name = driver.find_element(By.CSS_SELECTOR, '.form-group [name="last_name"]')
    input_l_name.send_keys("Bannikova")
    input_city = driver.find_element(By.CSS_SELECTOR, '.form-group .city')
    input_city.send_keys("Moscow")
    input_city = driver.find_element(By.CSS_SELECTOR, '[id="country"]')
    input_city.send_keys("Russia")
    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()
    
finally:
        # успеваем скопировать код за 30 секунд
        driver.close()
        time.sleep(30)
        driver.quit()
    
       # не забываем оставить пустую строку в конце файла
    





