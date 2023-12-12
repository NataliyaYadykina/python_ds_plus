# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def simple_numbers(n: int):
    count = 0
    numb = 2
    while count != n:
        for i in range(2, numb):
            if not numb % i:
                break
        else:
            count += 1
            yield numb
        numb += 1


for i in simple_numbers(10):
    print(i)
