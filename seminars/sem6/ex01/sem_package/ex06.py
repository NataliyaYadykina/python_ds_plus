# Задание №7
# Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную
# защищённую функцию.

__all__ = ['validate_date']

_MONTH_DAYS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

_YEAR_LOWER_LIMIT = 1
_YEAR_UPPER_LIMIT = 9999
_MONTH_LOWER_LIMIT = 1
_MONTH_UPPER_LIMIT = 12
_MONTH_START = 1
_FEBRUARY_END_LEAP = 29
_FEBRUARY_M = 2
_LEAP_MAIN_COND = 4
_LEAP_EXC_COND = 100
_LEAP_ADDITIONAL_COND = 100


def validate_date(date: str) -> bool:
    day, month, year = date.split('.')
    day = int(day)
    month = int(month)
    year = int(year)
    return _YEAR_LOWER_LIMIT <= year <= _YEAR_UPPER_LIMIT\
        and _MONTH_LOWER_LIMIT <= month <= _MONTH_UPPER_LIMIT\
        and __month_day_valid(day, month, year)


def __month_day_valid(day: int, month: int, year: int) -> bool:
    return ((_MONTH_START <= day <= _MONTH_DAYS[month])
            or (__leap_year(year)
                and month == _FEBRUARY_M
                and _MONTH_START <= day <= _FEBRUARY_END_LEAP))


def __leap_year(year: int) -> bool:
    return ((year % _LEAP_MAIN_COND == 0 and year % _LEAP_EXC_COND != 0)
            or year % _LEAP_ADDITIONAL_COND == 0)


if __name__ == "__main__":
    print(validate_date('31.10.2023'))
