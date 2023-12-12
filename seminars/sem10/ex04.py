# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь


class Person:

    def __init__(self, *args) -> None:
        *self.name, self.__age, self.city = args

    def birthday(self):
        self.__age += 1

    def show_age(self):
        return self.__age

    def full_name(self):
        return ' '.join(self.name)


class Employee(Person):

    def __init__(self, *args, id) -> None:
        super().__init__(*args)
        self.id = id
        self.access_level = sum(map(int, str(id))) % 7


if __name__ == "__main__":
    person1 = Person('Иванов', 'Петр', 'Сергеевич', 42, 'Липецк')
    person1.birthday()
    print(
        person1.show_age(),
        person1.full_name()
    )

    employee = Employee('Иванов', 'Петр', 'Сергеевич', 42, 'Липецк', id=981)
    employee.birthday()
    print(
        employee.show_age(),
        employee.full_name(),
        employee.id,
        employee.access_level
    )
