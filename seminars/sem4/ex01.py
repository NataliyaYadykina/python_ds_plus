# Задание №6
# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.


def print_string(user_str: str) -> None:
    """Print user string"""
    user_str = sorted(user_str.split(), reverse=True)
    max_len = len(max(user_str, key=len))

    for index, element in enumerate(user_str, 1):
        print(f'{index}, {element:>{max_len}}')


user_str = 'Hello, Beautiful World'
print_string(user_str)
