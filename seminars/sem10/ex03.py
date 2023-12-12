# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Person:

    def __init__(self, *args) -> None:
        *self.name, self.__age, self.city = args

    def birthday(self):
        self.__age += 1

    def show_age(self):
        return self.__age

    def full_name(self):
        return ' '.join(self.name)


if __name__ == "__main__":
    person1 = Person('Иванов', 'Петр', 'Сергеевич', 42, 'Липецк')
    person1.birthday()
    print(
        person1.show_age(),
        person1.full_name()
    )
