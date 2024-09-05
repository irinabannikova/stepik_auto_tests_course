import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/selects1.html")
time.sleep(2)

num_1 = driver.find_element(By.CSS_SELECTOR, "[id='num1']")
is_num_1 = num_1.text #получаем текст
int_num_1 = int(is_num_1)

num_2 = driver.find_element(By.CSS_SELECTOR, "[id='num2']")
is_num_2 = num_2.text  #получаем текст
int_num_2 = int(is_num_2)

sum_num = str(int_num_1 + int_num_2)

driver.find_element(By.TAG_NAME, "select").click()
driver.find_element(By.CSS_SELECTOR, f"[value='{sum_num}']" ).click()


driver.find_element(By.CSS_SELECTOR, "[type='submit']" ).click()
time.sleep(5)


driver.quit()