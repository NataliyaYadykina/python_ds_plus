# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
# s = пr**2

import decimal
from math import pi

decimal.getcontext().prec = 42
pi = decimal.Decimal(pi)
diameter = decimal.Decimal(50)
square = pi * diameter ** 2 / 4
long = pi * diameter

print(square, long)
