# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    """Documentation"""
    _instance = None

    def __init__(self, value, author) -> None:
        self.value = value
        self.author = author

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.old_values = []
            cls._instance.old_authors = []
        else:
            cls._instance.old_values.append(cls._instance.value)
            cls._instance.old_authors.append(cls._instance.author)
        return cls._instance

    def __str__(self) -> str:
        return f'{self.author=}, {self.value=}, {self.old_authors=}, {self.old_values=}'

    def __repr__(self) -> str:
        return f'Archive({self.value=}, {self.author=})'


archive1 = Archive('Hello world!', 'Nataliya')
print(archive1.old_values, archive1.old_authors)
print(archive1)
print(repr(archive1))

archive2 = Archive('more', 'Nata')
# print(archive1.old_values, archive1.old_authors)
print(archive2.old_values, archive2.old_authors)
print(archive2)

archive3 = Archive('more more', 'Natali')
# print(archive2.old_values, archive2.old_authors)
print(archive3.old_values, archive3.old_authors)
print(archive3.value, archive3.author)
