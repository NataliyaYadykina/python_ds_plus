# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import datetime
import logging
import argparse

logging.basicConfig(filename='seminars/sem15/log_ex05.log',
                    filemode='w', encoding='utf-8', level=logging.INFO,
                    format='{asctime}, {levelname}, {msg}', style='{')

MONTHS = (' ', 'янв', 'фев', 'мар',
          'апр', 'мая', 'июн',
          'июл', 'авг', 'сен',
          'окт', 'ноя', 'дек')

WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')


def transform_date(text: str):
    week_day_number = int(text[0])
    _, weekday, num_month = text.split()
    for wday_num, day in enumerate(WEEKDAYS):
        if day in weekday:
            weekday = wday_num
            break
    for month_num, month in enumerate(MONTHS):
        if month in num_month:
            num_month = month_num
            break
    count = 0
    for day in range(1, 32):
        try:
            temp_date = datetime.datetime(
                day=day, month=num_month,
                year=datetime.datetime.now().year)
        except ValueError as e:
            logging.error(msg=e)
        if temp_date.weekday() == weekday:
            count += 1
            if count == week_day_number:
                return temp_date


def cmd_launch():
    parser = argparse.ArgumentParser(prog='transform_date')
    parser.add_argument('-wc', '--week_count', default='1-й')
    parser.add_argument('-wd', '--week_day', default='понедельник')
    parser.add_argument('-m', '--month', default='января')
    args = parser.parse_args()
    return transform_date(f'{args.week_count} {args.week_day} {args.month}')


print(cmd_launch())

# в строке терминала набрать, например, для выполнения программы:
# python .\seminars\sem15\ex05.py -wc 4-й -wd четверг -m апреля
