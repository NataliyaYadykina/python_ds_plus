# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

import pathlib
import os


def sort_files():
    curr_path = pathlib.Path(os.getcwd() + '/seminars/sem7/')
    # print(curr_path)
    for file in curr_path.iterdir():
        # print(i)
        if file.suffix == '.py' or file.suffix == '.txt':
            continue
        try:
            file.replace(f'{curr_path}/{file.suffix}/{file.name}')
        except FileNotFoundError:
            os.mkdir(os.getcwd() + '/seminars/sem7/' + file.suffix)
            file.replace(f'{curr_path}/{file.suffix}/{file.name}')


if __name__ == "__main__":
    sort_files()
