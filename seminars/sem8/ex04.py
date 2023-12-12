# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import json


def csv2json(source_name: str, output_name: str):
    with (open(source_name, 'r', encoding='utf-8') as src,
          open(output_name, 'w', encoding='utf-8') as out):
        data = src.read().split('\n')
        header = data[0].split(',')
        result = []
        for user in data:
            list_user = user.split(',')
            if user and not list_user == header:
                result.append(
                    dict(zip(header, list_user)))
        json.dump(result, out, indent=4, ensure_ascii=False)


csv2json('seminars/sem8/ex02.csv', 'seminars/sem8/ex04.json')
