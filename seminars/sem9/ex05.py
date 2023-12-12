# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

import ex02
import ex03
import ex04


@ex04.decorator_func(3)
@ex03.save_json
@ex02.decorator_func
def game_numbers(number: int, count: int) -> bool:
    for _ in range(count):
        answer = int(input('Enter number: '))
        if answer == number:
            return True
    return False


print(game_numbers(3, 2))
