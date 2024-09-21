from math import gcd


def say_hello(name):
    return f"Hello, {name}"
#подставляет к имени hello
#x = say_hello('Irina')
#print(x)

def  get_hidden_card(string, base=4):
    masked_beginning = "*" * base
    len_end = len(string) - base
    not_masked_end = string[-len_end:]
    return f"{masked_beginning}{not_masked_end}"
#скрывает первый 4 цифры номера карты, base необяз парам по умолчанию
#x = get_hidden_card('123456789', 4)
#print(x)

def trim_and_repeat(string, offset=0, repetitions=1):
    cut_str = string[offset:]
    cut_repit = cut_str * repetitions
    return cut_repit
#выводит текст обрезая до 3 букв(сначала) и повторяя его 2 раза
#text='python'
#print(trim_and_repeat(text, offset=3, repetitions=2))  # honhon

def letter_multiply(text: str, letter: str, quantity_repiat: int) -> str:
    quantity_letter = letter * quantity_repiat
    result = text.replace(letter, quantity_letter)
    return result
#выводит слово с повторяющейся буквой. бука и число повторений - входные параметры
#text='python'
# print(letter_multiply(text, 'p', 2)) # => ppython

def get_age_difference(year_1: int, year_2: int) -> int:
    result = abs(year_1 - year_2)
    return f"The age difference is {result}"
# функцию принимает два года рождения и возвращает строку с разницей в возрасте в виде The age difference is 11.
# actual = get_age_difference(2001, 2018)
# print(actual)  # => The age difference is 17

def has_upper_case(text):
    return text.lower() != text 
# функция проверяет наличие заглавных букв в слове
# input_string1 = "Yyy"
# result1 = has_upper_case(input_string1)
# print(result1)  # True


def string_or_not(argument):
    return isinstance(argument, str) and 'yes' or 'no'
# функцию проверяет является ли переданный параметр строкой. Если да, то возвращается строка yes, иначе no.
# input_string1 = 10
# result1 = string_or_not(input_string1)
# print(result1) # no  

def normalize_url(address):
    protocol_1 = 'https://'
    protocol_2 = 'http://'
    first_chars = address[:8]
    if first_chars == protocol_1:
        correct_address = address
    elif address.startswith(protocol_2):
        return protocol_1 + address[len(protocol_2):]
    else:
        correct_address = protocol_1 + address
    return correct_address
#решение учителя
def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url
# функция выполняет нормализацию данных. Она принимает адрес сайта и возвращает его с https:// в начале.   
# input_string1 = 'google.com'
# result1 = normalize_url(input_string1)
# print(result1) # # https://google.com
    
def get_number_explanation(number):
    match number:
        case 666:
            return(f'devil number')
        case 42:
            return(f'answer for everything')
        case 7:
            return(f'prime number')
        case _:
            return(f'just a number')
#функция выводит разные сообщения в зависемости от вводимого числа


