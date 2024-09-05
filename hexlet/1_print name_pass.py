print('Enter your name:')
x = input()
print('Hello, ' + x)
print('Enter your password:')
x = input()
if x.strip() == '7': # strip Обрезает пробелы в начале и в конце строки
    print('success')
else:
    print('NO')

