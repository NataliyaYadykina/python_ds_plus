# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

from ex04 import User, load_users
from ex03 import (LevelProjectException,
                  AccessProjectException)


class Project:

    def __init__(self, filename) -> None:
        self.users = load_users(filename)
        self.admin = None

    def auth(self, name, id):
        base_user = User(name, id, None)
        if base_user not in self.users:
            raise AccessProjectException(base_user)
        for user in self.users:
            if user == base_user:
                self.admin = user

    def add_new_user(self, name, id, level):
        if self.admin.level > level:
            raise LevelProjectException(self.admin.level, level)
        self.users.add(User(name, id, level))


if __name__ == "__main__":
    process = Project('seminars/sem13/ex04_users.json')
    process.auth('Vlad', '1')
    process.add_new_user('test_user', '10', 3)
    print(process.users)

    process.auth('Vlad', '1')
    process.add_new_user('test_user', '10', 0)
    print(process.users)
