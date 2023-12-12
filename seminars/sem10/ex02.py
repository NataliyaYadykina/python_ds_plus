# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.width, self.length = args[0], args[0]
        elif len(args) == 2:
            self.width, self.length = args
        else:
            raise ValueError

    def get_square(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2


if __name__ == "__main__":
    rect1 = Rectangle(3)
    rect2 = Rectangle(4, 2)
    print(rect1.get_perimeter(), rect1.get_square(),
          rect2.get_perimeter(), rect2.get_square())
