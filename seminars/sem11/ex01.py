# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime


class MyStr(str):
    """Documentation"""

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now()
        return instance


my_str = MyStr('Hello world!', 'Nataliya')
print(my_str.author, my_str.time)
more_str = MyStr('more', 'Nata')
print(more_str.author, my_str.time)
print(my_str.author, my_str.time)
