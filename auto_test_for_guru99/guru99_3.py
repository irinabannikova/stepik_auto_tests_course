from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#проверка авторизации с невалидными данными

driver = webdriver.Firefox()

link = "https://www.demo.guru99.com/V4/index.php"
driver.get(link)

#невалидный логин+валидный пароль
input_email = driver.find_element(By.CSS_SELECTOR, "[name='uid']")
valid_login = 'mngr588094'
input_email.send_keys('testdu123')
input_password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
input_password.send_keys('EhebAva')
submit_button = driver.find_element(By.CSS_SELECTOR, "[value='LOGIN']")
submit_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
time.sleep(1)
alert.accept()

assert 'User or Password is not valid' == alert_text
print('невалидный логин/валидный пароль-тест пройден')
driver.quit()

#валидный логин+невалидный пароль
driver = webdriver.Firefox()

link = "https://www.demo.guru99.com/V4/index.php"
driver.get(link)

input_email = driver.find_element(By.CSS_SELECTOR, "[name='uid']")
valid_login = 'mngr588094'
input_email.send_keys(valid_login)
input_password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
input_password.send_keys('Eheakshjdb')
submit_button = driver.find_element(By.CSS_SELECTOR, "[value='LOGIN']")
submit_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
time.sleep(1)
alert.accept()

assert 'User or Password is not valid' == alert_text
print('валидный логин/невалидный пароль-тест пройден')
driver.quit()

#невалидный логин+невалидный пароль
driver = webdriver.Firefox()

link = "https://www.demo.guru99.com/V4/index.php"
driver.get(link)

input_email = driver.find_element(By.CSS_SELECTOR, "[name='uid']")
valid_login = 'mngr50000'
input_email.send_keys(valid_login)
input_password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
input_password.send_keys('Eheabhgvgc')
submit_button = driver.find_element(By.CSS_SELECTOR, "[value='LOGIN']")
submit_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
time.sleep(1)
alert.accept()

assert 'User or Password is not valid' == alert_text
print('невалидный логин/невалидный пароль-тест пройден')
driver.quit()




