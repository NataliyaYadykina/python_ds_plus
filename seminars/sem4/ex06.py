# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_numbers_between_indexes(
        numbers: list[int | float], index_1: int, index_2: int
) -> int | float:
    """Вернуть сумму чисел между между переданными индексами."""
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
    if index_1 < 0:
        index_1 = 0
    return sum(numbers[index_1:index_2 + 1:])


list_numbers = [1, 3, 2, 5, 2, 4, 6]
ind_1, ind_2 = 5, 2

print(sum_numbers_between_indexes(list_numbers, ind_1, ind_2))
