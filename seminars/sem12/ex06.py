# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


class Side:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < 0:
            raise ValueError


class Rectangle:
    width = Side()
    length = Side()

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

    def __add__(self, other: "Rectangle"):
        new_square = self.get_square() + other.get_square()
        new__width = self.width + other.width
        new_len = new_square / new__width
        return Rectangle(new__width, new_len)

    def __sub__(self, other: "Rectangle"):
        new_square = self.get_square() - other.get_square()
        new__width = self.width
        new_len = new_square / new__width
        return Rectangle(new__width, new_len)

    def __eq__(self, other: "Rectangle") -> bool:
        return self.get_square() == other.get_square()

    def __lt__(self, other: "Rectangle") -> bool:
        return self.get_square() < other.get_square()

    def __gt__(self, other: "Rectangle") -> bool:
        return self.get_square() > other.get_square()


if __name__ == "__main__":
    rect1 = Rectangle(4, 2)
    print(rect1.width, rect1.length)
    rect1.width = 5
    print(rect1.width)
    rect1.length = -1
    print(rect1.length)
