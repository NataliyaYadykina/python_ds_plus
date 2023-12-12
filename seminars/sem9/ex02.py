# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные
# в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from typing import Callable
from random import randint
from functools import wraps


def decorator_func(func: Callable):
    @wraps(func)
    def wrapper(number: int, count: int):
        if not 1 <= number <= 100:
            number = randint(1, 100)
        if not 1 <= count <= 10:
            count = randint(1, 10)
        return func(number, count)
    return wrapper


@decorator_func
def game_numbers(number: int, count: int) -> bool:
    for _ in range(count):
        answer = int(input('Enter number: '))
        if answer == number:
            return True
    return False


if __name__ == "__main__":
    # game = decorator_func(game_numbers)
    # game(2, 1)

    print(game_numbers(2, 1))
