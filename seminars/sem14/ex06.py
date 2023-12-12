# Задание №6
# На семинаре 13 был создан проект по работе с
# пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json


class BaseProjectException(Exception):
    pass


class LevelProjectException(BaseProjectException):

    def __init__(self, admin_level, new_user_level) -> None:
        self.admin_level = admin_level
        self.new_user_level = new_user_level

    def __str__(self) -> str:
        return (f'Ваш уровень {self.admin_level}'
                f'больше, чем {self.new_user_level}')


class AccessProjectException(BaseProjectException):
    def __init__(self, user: "User") -> None:
        self.user = user

    def __str__(self) -> str:
        return f'Пользователь {self.user} отсутствует'


class User:

    def __init__(self, name: str,
                 id: int, level: int) -> None:
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, __value: "User") -> bool:
        return self.name == __value.name and self.id == __value.id

    def __hash__(self) -> int:
        return int(self.id)+len(self.name)

    def __repr__(self) -> str:
        return f'{self.name} | {self.id}'


def load_users(filename: str) -> set[User]:
    try:
        with open(filename, 'r', encoding='utf-8') as src:
            users = json.load(src)
    except FileNotFoundError:
        users = []
    result = {User(name=user['name'],
                   id=user['id'],
                   level=int(user['level'])) for user in users}
    return result


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
    print(load_users('seminars/sem14/ex06_users.json'))

    process = Project('seminars/sem14/ex06_users.json')
    process.auth('Vlad', '1')
    process.add_new_user('test_user', '10', 3)
    print(process.users)

    process.auth('Vlad', '1')
    process.add_new_user('test_user', '10', 0)
    print(process.users)
