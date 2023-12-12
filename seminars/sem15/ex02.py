# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging

logging.basicConfig(filename='seminars/sem15/log_ex02.log',
                    filemode='w', encoding='utf-8', level=logging.INFO)


def decorator(func):
    logger = logging.getLogger(func.__name__)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'{func.__name__}: {result}, {args}, {kwargs}')
        return result
    return wrapper


@decorator
def func(*args):
    return sum(args)


@decorator
def str_func():
    return 'Hello, world!'


if __name__ == "__main__":
    print(str_func())
    print(func(4, 3))
