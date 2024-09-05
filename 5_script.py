from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    # ищем локатор которые пройдёт по всему списку 
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    # найдет все текстовые поля на странице с атрибутом type='text' и в каждое из них введет текст "Мой ответ" с помощью метода send_keys.
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# пустая строка