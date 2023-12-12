# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='seminars/sem15/log_ex01.log',
                    filemode='w', encoding='utf-8')


def do_smth(*args, **kwargs):
    try:
        return sum(args)
    except Exception as e:
        logging.error(msg=f'{e}, {args}, {kwargs}')


do_smth('sdf', 2)
