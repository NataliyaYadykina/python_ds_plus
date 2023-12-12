# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


def readline_(file):
    line = file.readline()
    if line == '':
        file.seek(0)
        return file.readline()
    return line


def write_with_join(
        names: str, numbers: str, result_name: str) -> None:
    with (
            open(names, 'r', encoding='utf-8') as names_f,
            open(numbers, 'r', encoding='utf-8') as numbers_f,
            open(result_name, 'w', encoding='utf-8') as result_f):
        list_name = names_f.read().split('\n')
        list_numbers = numbers_f.read().split('\n')
        max_len = max(len(list_name), len(list_numbers))
        for _ in range(max_len - 1):
            new_name = readline_(names_f)[:-1]
            new_int, new_float = readline_(
                numbers_f)[:-1].split('|')
            mult = int(new_int) * float(new_float)
            if mult < 0:
                result_f.write(f'{new_name.lower()} {abs(mult)}\n')
            elif mult > 0:
                result_f.write(f'{new_name.upper()} {int(mult)}\n')


write_with_join(
    'seminars/sem7/ex02.txt',
    'seminars/sem7/ex01.txt',
    'seminars/sem7/ex03.txt')
