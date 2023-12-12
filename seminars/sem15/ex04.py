# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import datetime
import logging

logging.basicConfig(filename='seminars/sem15/log_ex04.log',
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


if __name__ == "__main__":
    print(transform_date('6-я среда апреля'))
