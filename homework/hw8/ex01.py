# Ваша задача - написать программу, которая принимает на вход директорию
# и рекурсивно обходит эту директорию и все вложенные директории.
# Результаты обхода должны быть сохранены в нескольких форматах:
# JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

# Путь к файлу или директории: Абсолютный путь к файлу или директории.
# Тип объекта: Это файл или директория.
# Размер: Для файлов - размер в байтах, для директорий -
# размер, учитывая все вложенные файлы и директории в байтах.
# Важные детали:

# Для дочерних объектов (как файлов, так и директорий)
# укажите родительскую директорию.

# Для файлов сохраните их размер в байтах.

# Для директорий, помимо их размера, учтите размер всех файлов и директорий,
# находящихся внутри данной директории, и вложенных директорий.

# Программа должна использовать рекурсивный обход директорий,
# чтобы учесть все вложенные объекты.

# Результаты должны быть сохранены в трех форматах:
# JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

# Для обхода файловой системы вы можете использовать модуль os.

# Вам необходимо написать функцию traverse_directory(directory),
# которая будет выполнять обход директории и возвращать результаты
# в виде списка словарей.
# После этого результаты должны быть сохранены
# в трех различных файлах (JSON, CSV и Pickle)
# с помощью функций save_results_to_json,
# save_results_to_csv и save_results_to_pickle.

# {
#     'Path': 'geek/dir/file.pdf',
#     'Type': 'File'
#     'Size': 1457
# }

import os
import json
import csv
import pickle


def traverse_directory(directory: str) -> list[dict]:
    # directory = f'{os.getcwd()}\\seminars'
    result = []
    for dir_path, dir_name, file_name in os.walk(directory, topdown=False):
        dir_size = 0
        print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        if file_name:
            for file in file_name:
                temp_dict = {}
                path = f'{dir_path}\\{file}'
                temp_dict['Path'] = path
                temp_dict['Type'] = 'File'
                temp_dict['Parent'] = path.split('\\')[-2]
                file_size = os.path.getsize(path)
                temp_dict['Size'] = file_size
                result.append(temp_dict)
                dir_size += file_size
        temp_dict = {}
        if not dir_path == directory:
            temp_dict['Path'] = dir_path
            temp_dict['Type'] = 'Directory'
            temp_dict['Parent'] = dir_path.split('\\')[-2]
            temp_dict['Size'] = dir_size
            result.append(temp_dict)
    set_sizes(result, get_sizes(result))
    result = delete_parent_key(result)
    save_results_to_json(result, 'homework/hw8/results.json')
    save_results_to_csv(result, 'homework/hw8/results.csv')
    save_results_to_pickle(result, 'homework/hw8/results.pickle')
    print(result)


def get_sizes(list_dicts: list[dict]) -> dict:
    dict_parent_sizes = {}
    for item in list_dicts:
        parent = item['Parent']
        if dict_parent_sizes.get(parent):
            dict_parent_sizes[parent] += item['Size']
        else:
            dict_parent_sizes[parent] = item['Size']
    print(dict_parent_sizes)
    return dict_parent_sizes


def set_sizes(list_dicts: list[dict], dict_parent_sizes: dict) -> None:
    for item_dict in list_dicts:
        if item_dict['Size'] == 0:
            dir = item_dict['Path'].split('\\')[-1]
            item_dict['Size'] = dict_parent_sizes[dir]


def delete_parent_key(result: list[dict]) -> list[dict]:
    for item_dict in result:
        del item_dict['Parent']
    return result


def save_results_to_json(result: list[dict], json_name: str) -> None:
    with open(json_name, 'w') as json_file:
        json.dump(result, json_file)


def save_results_to_csv(result: list[dict], csv_name: str) -> None:
    with open(csv_name, 'w', encoding='utf-8') as output:
        write = csv.DictWriter(output, ["Path", "Type", "Size"])
        write.writeheader()
        write.writerows(result)


def save_results_to_pickle(result: list[dict], pickle_name: str) -> None:
    with open(pickle_name, 'wb') as out:
        pickle.dump(result, out)


traverse_directory('seminars')
