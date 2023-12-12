# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable


def numbers_decorator(number: int, count: int) -> Callable:
    def input_answer():
        for _ in range(count):
            answer = int(input('Enter number: '))
            if answer == number:
                return True
        return False
    return input_answer


if __name__ == "__main__":
    game = numbers_decorator(10, 4)
    print(game())
