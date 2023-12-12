# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.

from random import randint
from sys import argv


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
    # print(guessing_game(1, 10, 3))
    print(argv)
    _, a, b, c = argv
    print(guessing_game(int(a), int(b), int(c)))
