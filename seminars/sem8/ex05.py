# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import pickle
import os


def json2pickle():
    os_listdir = os.listdir(
        os.getcwd() + '/seminars/sem8/')
    for file in os_listdir:
        filename, ext = file.split('.')
        if ext == 'json':
            with (
                    open(
                        f'seminars/sem8/{file}', 'r') as src,
                    open(
                        f'seminars/sem8/{filename}.pickle', 'wb') as out):
                pickle.dump(json.load(src), out)


if __name__ == "__main__":
    json2pickle()
