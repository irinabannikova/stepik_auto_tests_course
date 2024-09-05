import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/math.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)

answer = driver.find_element(By.CSS_SELECTOR, "[id='answer']")
answer.send_keys(y)

robot_chek = driver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
robot_chek.click()

rule_button = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
rule_button.click()

submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()

time.sleep(6)

driver.quit()