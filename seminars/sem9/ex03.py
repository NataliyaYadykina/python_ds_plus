# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.

# [
#     {
#         "args": args,
#         **kwargs,
#         "result": result
#     }
# ]

import json
import os
from functools import wraps


def save_json(func: callable) -> callable:
    json_path = f'seminars/sem9/{func.__name__}.json'
    if f'{func.__name__}.json' in os.listdir(
            os.getcwd() + '/seminars/sem9/'):
        with open(json_path, 'r') as file:
            data = json.load(file)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(json_path, 'w') as file:
            result = func(*args, **kwargs)
            data.append({"args": args, **kwargs, "result": result})
            json.dump(data, file, indent=4)
        return result
    return wrapper


@save_json
def make_sum(*args, **kwargs):
    return sum(args)


@save_json
def fffff(a, b, c, reverse=True):
    if reverse:
        return [c, b, a]
    return [a, b, c]


if __name__ == "__main__":
    print(make_sum(1, 2, 17, four=4, five=5, six=6))
    print(fffff(1, 2, 3))
    print(fffff(1, b=4, c=3))
    print(fffff(10, 2, 30, reverse=False))
    print(fffff(111, 222, 333))
