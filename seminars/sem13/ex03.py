# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

from ex04 import User


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
    def __init__(self, user: User) -> None:
        self.user = user

    def __str__(self) -> str:
        return f'Пользователь {self.user} отсутствует'
