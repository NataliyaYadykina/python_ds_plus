# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json


def json_to_csv(json_name: str):
    name_out, _ = json_name.split('.')
    with open(json_name, 'r', encoding='utf-8') as source:
        data = json.load(source)
    result = []
    for access_level, user_data in data.items():
        for id, name in user_data.items():
            result.append(
                {"access_level": access_level,
                 "name": name,
                 "id": id})
    with open(f'{name_out}.csv', 'w', encoding='utf-8') as output:
        write = csv.DictWriter(output, ["access_level", "name", "id"])
        write.writeheader()
        write.writerows(result)


if __name__ == "__main__":
    json_to_csv('seminars/sem8/ex02.json')
