from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#проверка авторизации с валидными данными

driver = webdriver.Firefox()

link = "https://www.demo.guru99.com/V4/index.php"
driver.get(link)
#вводим емаил
input_email = driver.find_element(By.CSS_SELECTOR, "[name='uid']")
login = 'mngr588094'
input_email.send_keys(login)
#вводим пароль
input_password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
input_password.send_keys('EhebAva')

#клик на *войти*
submit_button = driver.find_element(By.CSS_SELECTOR, "[value='LOGIN']")
submit_button.click()

#удоствериться в авторизации
welcome_text = driver.find_element(By.CSS_SELECTOR, ".heading3[behavior='alternate']")
text = welcome_text.text

user_id = driver.find_element(By.CSS_SELECTOR, "tr[align='center']")
text_id = user_id.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Welcome To Manager's Page of Guru99 Bank" == text
print('авторизация успешна') 
assert f'Manger Id : {login}' == text_id
print('логин верный') 

driver.save_screenshot("screenshot.png")

driver.quit()

time.sleep(8)

driver.quit()


