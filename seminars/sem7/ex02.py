# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint
from random import choice

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


def _name_gen():
    return ''.join([choice(CONSONANTS) if i % 2
                    else choice(VOWELS)
                    for i in range(randint(4, 7))]).capitalize()


def pseudo_names(count_str: int, file_name: str):
    """ """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines([_name_gen() + '\n' for _ in range(count_str)])


pseudo_names(12, 'seminars/sem7/ex02.txt')
