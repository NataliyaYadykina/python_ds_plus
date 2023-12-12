# Напишите функцию группового переименования файлов
# в папке test_folder под названием rename_files.
# Она должна:
# a. принимать параметр желаемое конечное имя файлов. ***
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере. ***
# c. принимать параметр расширение исходного файла. ***
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла. ***
# e. принимать диапазон сохраняемого оригинального имени. ***
# Например для диапазона [3, 6] берутся буквы
# с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории ***
########################
# Пример использования.
# На входе:
# rename_files(desired_name="new_file_", num_digits=3,
# source_ext="txt", target_ext="doc")
# На выходе:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc,
# new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc,
# new_file_002.doc, new_file_009.doc, new_file_010.doc

import pathlib
import os


def rename_files(
        desired_name="new_file_",
        num_digits=3,
        source_ext="pdf",
        target_ext="txt",
        range_old_name=[],
        desired_name_end=""
):
    index = 1
    str_path = os.getcwd() + '/test_folder/'
    target_path = pathlib.Path(str_path)
    for file in target_path.iterdir():
        # print(file)
        if file.suffix == '.' + source_ext:
            counter_file = '0' * (num_digits - 1 - index // 10) + str(index)
            if range_old_name:
                old_name_part = file.name[
                    range_old_name[0]: range_old_name[1] + 1] + '_'
            else:
                old_name_part = ''
            # print(old_name_part)
            new_name = ''.join([str_path,
                               desired_name,
                               old_name_part,
                               desired_name_end,
                               counter_file,
                               '.' + target_ext
                                ])
            # print(new_name)
            file.rename(new_name)
            index += 1


rename_files()
