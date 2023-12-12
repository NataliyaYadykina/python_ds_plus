# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


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

    def __add__(self, other: "Rectangle"):
        new_square = self.get_square() + other.get_square()
        new_width = self.width + other.width
        new_len = new_square / new_width
        return Rectangle(new_width, new_len)

    def __sub__(self, other: "Rectangle"):
        new_square = self.get_square() - other.get_square()
        new_width = self.width
        new_len = new_square / new_width
        return Rectangle(new_width, new_len)

    def __eq__(self, other: "Rectangle") -> bool:
        return self.get_square() == other.get_square()

    def __lt__(self, other: "Rectangle") -> bool:
        return self.get_square() < other.get_square()

    def __gt__(self, other: "Rectangle") -> bool:
        return self.get_square() > other.get_square()


if __name__ == "__main__":
    rect1 = Rectangle(5)
    rect2 = Rectangle(4, 2)
    print(rect1 == rect2)
    print(rect1 > rect2)
    print(rect1 > rect1)
