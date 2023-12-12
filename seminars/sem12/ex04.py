# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.


class Rectangle:

    def __init__(self, *args) -> None:
        if len(args) == 1 and args[0] > 0:
            self._width, self._length = args[0], args[0]
        elif len(args) == 2 and args[0] > 0 and args[1] > 0:
            self._width, self._length = args
        else:
            raise ValueError

    def get_square(self):
        return self._length * self._width

    def get_perimeter(self):
        return (self._length + self._width) * 2

    def __add__(self, other: "Rectangle"):
        new_square = self.get_square() + other.get_square()
        new__width = self._width + other._width
        new_len = new_square / new__width
        return Rectangle(new__width, new_len)

    def __sub__(self, other: "Rectangle"):
        new_square = self.get_square() - other.get_square()
        new__width = self._width
        new_len = new_square / new__width
        return Rectangle(new__width, new_len)

    def __eq__(self, other: "Rectangle") -> bool:
        return self.get_square() == other.get_square()

    def __lt__(self, other: "Rectangle") -> bool:
        return self.get_square() < other.get_square()

    def __gt__(self, other: "Rectangle") -> bool:
        return self.get_square() > other.get_square()

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError


if __name__ == "__main__":
    rect1 = Rectangle(4, -2)
    print(rect1.width, rect1.length)
    rect1.width = 5
    print(rect1.width)
    # rect1.length = -1
