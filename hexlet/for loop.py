from random import choice
from random import randint


def filter_string(text, char):
    result = '' #инициализация переменной result, которая будет хранить отфильтрованную строку.
    lowered_char = char.lower() #приведение символа char к нижнему регистру и сохранение его в переменной lowered_char. 
    #Это делается для того, чтобы учесть как символы верхнего, так и нижнего регистра при фильтрации.
    for current_char in text: # Мы начинаем цикл, который будет перебирать каждый символ в строке text. 
            #Переменная current_char будет поочередно принимать значение каждого символа из text.
        if current_char.lower() != lowered_char:# Мы проверяем условие: если текущий символ (приведенный к нижнему регистру) не равен символу char (также приведенному к нижнему регистру), 
            #то выполняем следующий блок кода.
            result= result + current_char  #Мы добавляем текущий символ к результату result, если он не равен символу char.
    return result.strip() #Мы возвращаем отфильтрованную строку result, 
#удаляя возможные пробелы в начале и в конце строки с помощью метода strip().
    

def upper_char(string):
    result = '' #инициализация переменной result, которая будет хранить отфильтрованную строку
    for char in string: #Мы начинаем цикл, который будет перебирать каждый символ в строке string. 
            #Переменная char будет поочередно принимать значение каждого символа из string.
        if char == char.upper():#если символ равен большому символу ТО
           result = result + char #добавляем к отфильтрованной строке этот символ
    return result #Мы возвращаем отфильтрованную строку result
#функция принемает на вход строку.  вней большие и маленькие буквы, надо чтобы вывелись только большие.

def count_char(string, user_char):
    count = 0
    for char in string:
        if char == user_char:
            count +=1
    return count
#функция принемает на вход строку и букву. надо посчитать, сколько раз буква повторяется.
    
def filter_string2(string, user_char):
    result =''
    user_char = user_char.lower()
    for char in string:
        if char.lower() != user_char:
            result = result + char
    return result.strip()

#функция принимает на вход слово, определяет, является ли оно палиндромом и возвращает T или F

def is_palindrome(string):
    text = string.lower()
    start_i = 0 
    end_i = -1
    for char in text:
        if text[start_i] != text[end_i]:
         return False
        start_i += 1
        end_i -= 1
    return True 
# функция проверяет гласная ли буква
def is_vowel(char):
    vowels = 'aeiouyауоыиэяюёе'
    return char.lower() in vowels

# функция считает и возвращает количество гласных букв в ней.
# используйте функцию is_vowel()

def count_vowels(string):
    result =''
    for char in string:
        if is_vowel(char) == True:
         result = result + char
    return len(result)


#функция принимает строку-набор и возвращает случайный символ по индексу из ограниченного диапазона

def choice_from_range(string, start_i, end_i):
    random_number = randint(start_i, end_i)
    char = string[random_number]
    return char

#принимает пару (кортеж из двух значений) и возвращает пару, значения которой расположены строго в порядке возрастания.
def sort_pair(pair):
    a, b = pair
    if a <= b:
        return (a, b)
    else:
        return (b, a)
    

def is_happy_ticket(ticket):
    half_string = len(ticket) // 2
    i_start = ticket[:half_string]
    # sum_start = sum(int(digit) for digit in i_start)
    sum_start = 0
    for digit in i_start:
        sum_start += int(digit)
    i_end = ticket[half_string:]
    sum_end = 0
    for digit in i_end:
        sum_end += int(digit)
    #sum_end = sum(int(d) for d in i_end)
    return sum_start == sum_end
    



    

