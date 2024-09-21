import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_auth_pz():
    driver = webdriver.Chrome()
    driver.get('https://positronica.ru/')
    time.sleep(7)

    driver.find_element(By.XPATH, '//button[@title="Войти" and @type="button"]').click() # клик на вход
    time.sleep(10)

    driver.find_element(By.XPATH, '//button[@title="Войти по почте"]').click() # клик на войти по почте
    time.sleep(10)

    driver.find_element(By.XPATH, '//input[@id="USER_LOGIN"]').send_keys("test_iser1@mail.ru") # ввод email
    driver.find_element(By.XPATH, '//input[@id="USER_PASSWORD"]').send_keys("qwerty") # ввод pass
    driver.find_element(By.XPATH, '//button[@title="Войти" and @type="submit"]').click() # клик на вход
    time.sleep(3)

    try:
        driver.find_element(By.XPATH, '//a[@title="Выход"]')
    except NoSuchElementException:
        print('авторизация не успешна')
    else:
        print('авторизация успешна')
    finally:
        driver.quit()

