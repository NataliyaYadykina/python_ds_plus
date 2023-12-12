# В организации есть два типа людей:
# сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

# Фамилия (строка, не пустая)
# Имя (строка, не пустая)
# Отчество (строка, не пустая)
# Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.

# Ваша задача:

# Создать класс Person, который будет иметь атрибуты
# и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных
# и генерировать исключения InvalidNameError и InvalidAgeError,
# если данные неверные.

# Создать класс Employee, который будет наследовать класс Person
# и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID
# и генерировать исключение InvalidIdError, если ID неверный.

# Добавить метод birthday в класс Person,
# который будет увеличивать возраст человека на 1 год.

# Добавить метод get_level в класс Employee,
# который будет возвращать уровень сотрудника
# на основе суммы цифр в его ID (по остатку от деления на 7).

# Создать несколько объектов класса Person и Employee с разными данными
# и проверить, что исключения работают корректно при передаче неверных данных.


class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:

    def __init__(self, fathername: str, firstname: str,
                 lastname: str, age: int) -> None:
        self.fathername = self.check_name(fathername)
        self.firstname = self.check_name(firstname)
        self.lastname = self.check_name(lastname)
        self.age = self.check_age(age)

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def check_name(self, name):
        if name:
            return name
        else:
            raise InvalidNameError(
                f'Invalid name: {name}. Name should be a non-empty string.')

    def check_age(self, age):
        if isinstance(age, int) and age > 0:
            return age
        else:
            raise InvalidAgeError(
                f'Invalid age: {age}. Age should be a positive integer.')


class Employee(Person):

    def __init__(self, fathername: str, firstname: str,
                 lastname: str, age: int, id_user) -> None:
        super().__init__(fathername, firstname, lastname, age)
        self.id_user = self.check_id(id_user)

    def get_level(self):
        return

    def check_id(self, id: int):
        if isinstance(id, int) and len(str(id)) == 6:
            return id
        else:
            raise InvalidIdError(
                f'Invalid id: {id}. Id should be a 6-digit '
                f'positive integer between 100000 and 999999.')


if __name__ == "__main__":
    # person = Person('', 'John', 'Doe', 30)
    # person = Person('Alice', 'Smith', 'Johnson', -5)
    employee = Employee('Bob', 'Johnson', 'Brown', 40, 123451)
    print(employee.get_age())
