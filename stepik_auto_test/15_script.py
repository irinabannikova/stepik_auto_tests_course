import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()  # Максимизируем окно браузера

link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

browser.switch_to.window(browser.window_handles[1]) # перейти на первую вкладку которая открылась



element_x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = element_x.text #получаем текст

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer_text = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
answer_text.send_keys(y)


submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']" )
submit_button.click()
time.sleep(5)


browser.quit()