import time
import math
def decorator(func):
    def functime():
        start = time.time()
        print(('Была вызвана функция', func.__name__))
        func()
        end = time.time()
        print('Время выполнения функции: {} секунд.'.format(end - start))
    return functime

@decorator
def ex_1():
    width = float(input('Введите длину участка в футах\n'))
    length = float(input('Введите ширину участка в футах\n'))
    SQFT_PER_ACRE = (length*width)/43560

    print('Площадь участка в акрах = ', SQFT_PER_ACRE)

@decorator
def ex_2():
    A = 9.8
    d = float(input('Введите высоту в метрах\n'))
    vf = math.sqrt(2 * A * d)
    print("Скорость в момент столкновения ", vf, " м/с")

print('>> Старт')
ex_1()
ex_2()
print('>> Конец')

