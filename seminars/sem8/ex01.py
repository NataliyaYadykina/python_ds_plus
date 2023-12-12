# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def from_txt_to_json(txt_file_name: str, json_file_name: str):
    with (
        open(txt_file_name, 'r', encoding='utf-8') as txt_file,
        open(json_file_name, 'w') as json_file
    ):
        text = txt_file.readlines()
        json.dump({
            i.split(' ')[0]: i.split(' ')[1][:-1]
            for i in text},
            json_file)


from_txt_to_json(
    'seminars/sem8/ex01.txt',
    'seminars/sem8/ex01.json')
