# Напишите функцию get_file_info,
# которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

# file_path = '/home/user/docs/my.file.with.dots.txt'
# Ожидаемый ответ:
# ('/home/user/docs/', 'my.file.with.dots', '.txt')

# file_path = '/home/user/data/file'
# Ожидаемый ответ:
# ('/home/user/data/', '', '.file')

file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    *first, second = file_path.split('/')
    path_file = ''.join([i + '/' for i in first])

    if second.count('.') > 0:
        *name_file, extension_file = second.split('.')
        name_file = '.'.join(name_file)
        extension_file = '.' + extension_file
    else:
        name_file, extension_file = '', '.' + second
    return path_file, name_file, extension_file


print(get_file_info(file_path))
