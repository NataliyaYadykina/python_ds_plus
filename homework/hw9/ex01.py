# Создайте функцию generate_csv_file(file_name, rows),
# которая будет генерировать по три случайны числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл.
# Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных,
# которые нужно сгенерировать.
# Создайте функцию find_roots(a, b, c),
# которая будет находить корни квадратного уравнения
# вида ax^2 + bx + c = 0. Функция принимает три аргумента:
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
# Создайте декоратор save_to_json(func),
# который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции,
# исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения
# с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json.
# Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file
# и find_roots в файле results.json будет сохранена информация
# о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
# Пример
# На входе:
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")

# with open("results.json", 'r') as f:
#     data = json.load(f)

# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"
#           Количество строк в файле не находится в диапазоне от 100 до 1000.")

# print(len(data)==101)
# На выходе:
# True
# True

from random import randint
import json


def generate_csv_file(file_name: str, rows: int):
    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(rows):
            file.write(
                f'{randint(-100, 100)},\
{randint(-100, 100)},{randint(-100, 100)}\n')


def find_roots(name_file: str):
    add_path = 'homework/hw9/'
    results = []
    with (
        open(f'{add_path}{name_file}', 'r', encoding='utf-8') as file,
        open(f'{add_path}results.json', 'w', encoding='utf-8') as f_json
    ):
        for _ in file:
            results.append({1: 2})
        json.dump(results, f_json, indent=4)


# def find_roots(a: int, b: int, c: int):
#     d = b * b - 4 * a * c
#     if d > 0:
#         sqrtD = d ** (1/2)
#         x1 = (-b + sqrtD)/(2 * a)
#         x2 = (-b - sqrtD)/(2 * a)
#         return x1, x2
#     elif d == 0:
#         x = -b / (2 * a)
#         return x
#     else:
#         return None


generate_csv_file('homework/hw9/numbers.csv', 7)
find_roots('numbers.csv')
