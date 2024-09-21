from random import choice
from random import randint

def print_numbers(number):
    i = number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')
#Функция print_numbers(). Функция должна принимать число и выводить числа в обратном порядке от этого числа до нуля (нуль не выводится).
#По окончании работы функция должна вывести на экран строку finished!.
#print_numbers(4)
# => 4

def join_numbers_from_range(begin, end):
    i = begin # первая цифра которую брать в цикл(счётчик)
    result = '' # где я сохраню результат
    while i <= end: #пока begin меньше или равен еnd - цикл выполняется
        #print(f"Result: {result}")
        result = result + str(i) # пустая строка = строка соединить с строкой I (именно str Иначе не сделать конкотенацию)
        i = i + 1 # путь к следующему числу цикла
    return result
    
def my_substr(string, lenght):
    i = 0
    result = ''
    while i <= lenght:
        result = string[:i]
        i = i + 1
    return result
# ф-ция извлекает из строки подстроку указанной длины. Она принимает на вход два аргумента (строку и длину) и возвращает подстроку, начиная с первого символа:
# string = 'If I look back I am lost'
# print(my_substr(string, 7))  # => 'If I lo'

def has_char(string, char):
    index = 0 #инициализируем переменную index значением 0-для отслеживания текущего индекса символа в строке string.
    uppercase_char = char.upper() #символ char в верхний регистр с помощью метода upper()-чтобы сравнивать символы без учета регистра.
    while index < len(string):#Это начало цикла while, который будет выполняться, пока index меньше длины строки string.
        if string[index].upper() == uppercase_char:# Здесь мы сравниваем символ в позиции index строки string, преобразованный в верхний регистр, с символом uppercase_char. 
            #Если символы совпадают, то функция возвращает True, что означает, что символ найден.
            return True
        index += 1
    return False
# решение курса
# has_char()-должна проверять, содержит ли строка указанную букву (вне зависимости от регистра). 
# возвращает результат проверки – булево значение.
# print(has_char('Hexlet', 'H'))  # => True


def has_char_2(text, char):
    i = 0
    while len(text) > i:
        if text[i] == char:
         return True
        elif text[i] == char.upper():
         return True 
        elif text[i] == char.lower():
            return True 
        i= i + 1
    return False
# моё решение