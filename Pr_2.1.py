#23

from math import tan, pi
length = float(input('Введите длину сторон:\n'))
num = int(input('Введите число сторон:\n'))
s = (num * length ** 2) / (4 * tan(pi / num))
print('Площадь многоугольника = ', s)

# 7

num = int(input('Введите положительное число:\n'))
summ = num * (num + 1) / 2
print('Сумма чисел = ', summ)

# 37

sym = input('Введите букву латинского алфавита:\n')
if sym == "a" or sym == "e" or sym == "i" or sym == "o" or sym == "u" \
     or sym == "A" or sym == "E" or sym == "I" or sym == "O" or sym == "U":
    print('Гласная')
elif sym == "y" or sym == "Y":
    print('Как гласная, так и согласная')
else:
    print('Согласная')
