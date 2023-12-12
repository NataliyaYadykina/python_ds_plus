# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from string import ascii_letters
from random import randint
from random import choice


def _name_gen(min_name, max_name):
    return 'seminars/sem7/ex04_' + ''.join(
        [choice(ascii_letters)
         for i in range(randint(min_name, max_name))])


def create_file(
        extension='.txt',
        min_len_name=6,
        max_len_name=30,
        min_byte=256,
        max_byte=4096,
        count_file=42
) -> None:
    for _ in range(count_file):
        with open(
                _name_gen(min_len_name, max_len_name) + extension,
                'wb') as file:
            file.write(bytes([randint(0, 255)
                              for i in range(randint(min_byte, max_byte))]))


create_file(extension='.doc', count_file=3)
