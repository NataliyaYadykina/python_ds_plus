# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


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


if __name__ == "__main__":
    factorial1 = Factorial(3)
    print(factorial1(4), factorial1(5), factorial1(6))
    print(factorial1.show_history())
    print(factorial1(7), factorial1(8))
    print(factorial1.show_history())
