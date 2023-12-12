# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

user_str = 'Hello, Beautiful World'
user_str = sorted(user_str.split(), reverse=True)
max_len = len(max(user_str, key=len))

for index, element in enumerate(user_str, 1):
    print(f'{index}, {element:>{max_len}}')
