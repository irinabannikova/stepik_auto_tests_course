import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_comparision_pz():
    driver = webdriver.Chrome()
    driver.get('https://positronica.ru/product/ruchnoy-pylesos-rekam-hvvc-1150-chernyy-krasnyy-1901000016-1655736/')
    time.sleep(7)

    comparision_button = driver.find_element(By.CSS_SELECTOR, '[title="Добавить в сравнение"]')
    #извлекаем id товара и записываем его в переменную
    id = comparision_button.get_attribute('data-id')
    comparision_button.click()
    time.sleep(3)

    comparision_count_header = driver.find_element(By.XPATH, '//span[@class="menu__count compare_count" and text()="1"]')
    time.sleep(5)

    assert comparision_count_header, 'каунтер не проставлен'
    print('каунтер проставлен')

    link_comparision = driver.find_element(By.CSS_SELECTOR, '.menu__link[title ="Сравнение"] .menu__title')
    link_comparision.click()
    time.sleep(10)

    product_id_comparision = driver.find_element(By.CSS_SELECTOR, f"#product_{id}")

    assert product_id_comparision, 'товар не добавлен в сравнение'
    print('товар добавлен в сравнение')



