import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/get_attribute.html")
box_element = driver.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
x = box_element.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer = driver.find_element(By.CSS_SELECTOR, "[id='answer']")
answer.send_keys(y)


the_robot = driver.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
is_chek_robot = the_robot.get_attribute("checked")
if is_chek_robot is None:  # Чекбокс не выбран
   the_robot.click()

chek_rule = driver.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
chek_rule.click()


submit_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()
time.sleep(6)

driver.quit()
