# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json


class Factorial:

    def __init__(self, count) -> None:
        self.count = count
        self.history = []

    def __call__(self, number):
        for i in range(1, number):
            number *= i
        self.update(number)
        return number

    def update(self, number):
        if len(self.history) == self.count:
            self.history.pop(0)
        self.history.append(number)

    def show_history(self):
        return self.history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('seminars/sem12/ex02.json', 'w', encoding='utf-8') as file:
            json.dump(self.history, file)


if __name__ == "__main__":
    with Factorial(3) as obj:
        obj(2)
        obj(3)
        obj(4)
        obj(5)
