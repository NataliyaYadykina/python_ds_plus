# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def unicode_dict(user_str: str) -> dict:
    """
    Функция получает на вход строку из двух чисел через пробел.
    Сформируйте словарь, где ключом будет
    символ из Unicode, а значением — целое число.
    Диапазон пар ключ-значение от наименьшего из введённых
    пользователем чисел до наибольшего включительно.
    """
    start, stop = map(int, user_str.split())
    dict_result = {}
    for i in range(start, stop + 1):
        dict_result[chr(i)] = i
    return dict_result


user_str = '1 5'
print(unicode_dict(user_str))