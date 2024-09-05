import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# ищем кнопку войти на странице и кликаем на неё
auth = driver.find_element(By.CSS_SELECTOR, 'a.navbar__auth_login')
auth.click()
time.sleep(10)

#авторизация. вводим логин
login = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]')
login.send_keys("derwan45@mail.ru")
time.sleep(5)

#авторизация. вводим пароль
password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
password.send_keys("847656")
time.sleep(5)

#клик на кнопку войти
exit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
exit.click()
time.sleep(5)


# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(20)

#После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
