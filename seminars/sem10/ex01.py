# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from math import pi


class Circle:

    def __init__(self, rad: int | float) -> None:
        self.radius = rad

    def get_length(self):
        return 2 * pi * self.radius

    def get_area(self):
        return pi * self.radius ** 2


if __name__ == "__main__":
    circle = Circle(4)
    print(circle.get_length(), circle.get_area())
