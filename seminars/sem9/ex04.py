# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable
from functools import wraps


def decorator_func(count_repeat: int):
    def my_func(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_list = []
            for _ in range(count_repeat):
                arg_list.append(func(*args, **kwargs))
            return arg_list
        return wrapper
    return my_func


@decorator_func(3)
def game_numbers(number: int, count: int) -> bool:
    for _ in range(count):
        answer = int(input('Enter number: '))
        if answer == number:
            return True
    return False


print(game_numbers(3, 2))
