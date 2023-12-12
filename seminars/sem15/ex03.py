# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging

logging.basicConfig(filename='seminars/sem15/log_ex03.log',
                    filemode='w', encoding='utf-8', level=logging.INFO,
                    format='{asctime}, {levelname}, {msg}', style='{')


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
