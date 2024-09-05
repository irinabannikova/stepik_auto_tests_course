from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(5)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)# запускаем скрипт который скролит страницу до нужного элемента
#browser.execute_script("window.scrollBy(0, 100);") # скролит на 100пх вниз
time.sleep(5)
button.click()
time.sleep(5)