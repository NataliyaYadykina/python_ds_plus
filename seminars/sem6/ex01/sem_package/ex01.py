# Задание №2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint


def guessing_game(start, stop, count):
    num = randint(start, stop)
    for _ in range(count):
        user_num = int(input('Enter num: '))
        if user_num == num:
            print('You win!')
            return True
        elif user_num > num:
            print('less')
        else:
            print('more')
    else:
        print("You didn't the number.")
        return False


if __name__ == '__main__':
    print(guessing_game(1, 10, 3))
