import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()  # Максимизируем окно браузера


link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

element_x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = element_x.text #получаем текст

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

browser.execute_script("window.scrollBy(0, 150);")

answer_text = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
answer_text.send_keys(y)


the_robot = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
is_chek_robot = the_robot.get_attribute("checked")
the_robot.click()


the_rule = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
is_radio_robot = the_rule.get_attribute("checked")
if is_chek_robot is None:  # если чекбокс не выбран
   the_rule.click() # сделай клик

submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']" )
submit_button.click()
time.sleep(5)

