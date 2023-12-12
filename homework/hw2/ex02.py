# На вход автоматически подаются две строки frac1 и frac2
# вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать
# сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
# Пример
# На входе:
# frac1 = "1/2"
# frac2 = "1/3"
# На выходе:
# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

from fractions import Fraction

frac1 = "1/4"
frac2 = "2/3"


num1, den1 = map(int, frac1.split('/'))
num2, den2 = map(int, frac2.split('/'))


# defining a function to calculate LCM
def calculate_lcm(x, y):
    # selecting the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

# print("The L.C.M. of", den1,"and", den2,"is", calculate_lcm(den1, den2))


def add_and_multiply_simple_fractions(num1, den1, num2, den2):
    lcm = calculate_lcm(den1, den2)
    sum_num = lcm // den1 * num1 + lcm // den2 * num2
    sum_den = lcm
    prod_num = num1 * num2
    prod_den = den1 * den2
    return (sum_num, sum_den, prod_num, prod_den)


result = add_and_multiply_simple_fractions(
    num1, den1, num2, den2
)
sum_num, sum_den = result[0], result[1]
prod_num, prod_den = result[2], result[3]

# print('Дробь 1: {}/{}'.format(num1, den1))
# print('Дробь 2: {}/{}'.format(num2, den2))

# print('Сумма:\n числитель: {}\n знаменатель: {}'.format(sum_num, sum_den))
# print('Произведение:\n числитель: {}\n знаменатель: {}'
#   .format(prod_num, prod_den))

print(f"Сумма дробей: {sum_num}/{sum_den}")
print(f"Произведение дробей: {prod_num}/{prod_den}")


def add_and_multiply_fractions(frac1, frac2):
    frac1 = Fraction(frac1)
    frac2 = Fraction(frac2)
    sum_frac = frac1 + frac2
    prod_frac = frac1 * frac2

    return sum_frac, prod_frac


sum_frac, prod_frac = add_and_multiply_fractions(frac1, frac2)
print("Сумма дробей:", sum_frac)
print("Произведение дробей:", prod_frac)
