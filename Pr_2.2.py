NEW_BASE = 2
num = int(input('Введите десятичное число: '))
result = ''
bin_num = num
rem = bin_num % NEW_BASE
result = str(rem) + result
bin_num = bin_num // NEW_BASE
while bin_num > 0:
    rem = bin_num % NEW_BASE
    result = str(rem) + result
    bin_num = bin_num // NEW_BASE
print(num, 'в десятичной = ', result, 'в двоичной')
