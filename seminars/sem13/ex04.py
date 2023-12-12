# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json


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


if __name__ == "__main__":
    print(load_users('seminars/sem13/ex04_users.json'))
