# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

for i in range(1, 100):
    if not i % 15:
        print('FizzBuzz')
    elif not i % 3:
        print('Fizz')
    elif not i % 5:
        print('Buzz')
    else:
        print(i)

print('*' * 10)

gen_list = (
    'FizzBuzz' if not i % 15 else
    'Fizz' if not i % 3 else
    'Buzz' if not i % 5 else
    i for i in range(1, 100)
)

print(*gen_list, sep='\n')
