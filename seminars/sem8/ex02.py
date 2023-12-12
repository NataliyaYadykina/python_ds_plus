# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
# {
#     '1': {
#         '1': 'name1',
#         '2': 'name2'
#     },
#     '2': {
#         '3': 'name3',
#         '4': 'name4'
#     }
# }

import json
import os


def add_user(json_name: str) -> None:
    if json_name not in os.listdir(
            os.getcwd() + '/seminars/sem8/'):
        with open(json_name, 'w', encoding='utf-8') as json_file:
            json_file.write('{}')

    json_dict = {}
    with open(json_name, 'r', encoding='utf-8') as json_file:
        json_dict = json.load(json_file)
    while True:
        name = input('Enter your name: ')
        id = input('Enter your id: ')
        access_level = input('Enter your access level: ')
        json_dict[access_level] = json_dict.get(access_level, {})
        json_dict[access_level][id] = name
        with open(json_name, 'w', encoding='utf-8') as json_file:
            json.dump(json_dict, json_file, ensure_ascii=False)


add_user('seminars/sem8/ex02.json')
