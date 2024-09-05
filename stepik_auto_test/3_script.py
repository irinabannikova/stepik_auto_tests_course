from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://suninjuly.github.io/simple_form_find_task.html")


# если в коде внутри блока try произойдет какая-то ошибка, 
# то код внутри блока finally выполнится в любом случае


try:
    input_name = driver.find_element(By.CSS_SELECTOR, '.form-group [name="first_name"]')
    input_name.send_keys("Irina")
    input_l_name = driver.find_element(By.CSS_SELECTOR, '.form-group [name="last_name"]')
    input_l_name.send_keys("Bannikova")
    input_city = driver.find_element(By.CSS_SELECTOR, '.form-group .city')
    input_city.send_keys("Moscow")
    input_city = driver.find_element(By.CSS_SELECTOR, '[id="country"]')
    input_city.send_keys("Russia")
    submit_button = driver.find_element(By.CSS_SELECTOR, '[id="submit_button"]')
    submit_button.click()

finally:
    # закрываем браузер после всех манипуляций
    driver.close()
    time.sleep(30)
    driver.quit()

