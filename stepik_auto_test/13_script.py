import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
browser.maximize_window()  # Максимизируем окно браузера


link = "https://suninjuly.github.io/file_input.html"
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, ".form-group [name='firstname']")
first_name.send_keys("Irina")

last_name = browser.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']")
last_name.send_keys("Bannikova")

email = browser.find_element(By.CSS_SELECTOR, ".form-group [name='email']")
email.send_keys("derwan45@mail.ru")


current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)


element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)


submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_button.click()
time.sleep(5)

browser.quit()