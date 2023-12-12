# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle


def csv2pickledumps(source_name: str) -> str:
    with open(source_name, 'r', encoding='utf-8') as src:
        data = [row.split(',')
                for row in src.read().split('\n') if row]
    return pickle.dumps(data)


if __name__ == "__main__":
    result = csv2pickledumps('seminars/sem8/ex02.csv')
    print(result)
    print(pickle.loads(result, encoding='utf-8'))
