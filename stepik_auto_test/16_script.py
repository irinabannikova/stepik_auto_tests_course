from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
 

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
# странице будет найден элемент с id 'price', и в этом элементе будет присутствовать текст '$100'. 
# Если текст появляется внутри указанного элемента в течение 12 секунд, то это условие будет выполнено, и переменной price будет присвоено значение True. 
# Если текст не появляется в течение указанного времени, будет вызвано исключение TimeoutException.
price = WebDriverWait(browser, 12).until(
        EC. text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

book_button = browser.find_element(By.ID, 'book')
book_button.click()

element_x = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = element_x.text #получаем текст

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer_text = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
answer_text.send_keys(y)


submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']" )
submit_button.click()

time.sleep(8)