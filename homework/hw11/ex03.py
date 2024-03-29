# Разработайте программу для работы с прямоугольниками.
# Необходимо создать класс Rectangle,
# который будет представлять прямоугольник
# с заданными шириной и высотой.
# Атрибуты класса:
# width (int): Ширина прямоугольника.
# height (int): Высота прямоугольника.
# Методы класса:
# __init__(self, width, height=None): Конструктор класса.
# Принимает ширину и высоту прямоугольника.
# Если высота не указана (по умолчанию None),
# то считается, что прямоугольник является квадратом,
# и высота устанавливается равной ширине.
# perimeter(self): Метод для вычисления периметра прямоугольника.
# Возвращает целое число - значение периметра.
# area(self): Метод для вычисления площади прямоугольника.
# Возвращает целое число - значение площади.
# __add__(self, other): Магический метод,
# который определяет операцию сложения (+) для двух прямоугольников.
# Принимает другой прямоугольник other.
# Создает новый прямоугольник, который представляет собой
# объединение исходных прямоугольников по периметру.
# Возвращает новый прямоугольник.
# __sub__(self, other): Магический метод,
# который определяет операцию вычитания (-) одного прямоугольника из другого.
# Принимает вычитаемый прямоугольник other.
# Создает новый прямоугольник,
# представляющий разницу периметров исходных прямоугольников,
# и вычисляет высоту на основе этой разницы.
# Возвращает новый прямоугольник.
# __lt__(self, other): Магический метод,
# который определяет операцию "меньше" (<) для двух прямоугольников.
# Принимает другой прямоугольник other.
# Возвращает True, если площадь первого прямоугольника
# меньше площади второго, иначе False.
# __eq__(self, other): Магический метод,
# который определяет операцию "равно" (==) для двух прямоугольников.
# Принимает другой прямоугольник other.
# Возвращает True, если площади равны, иначе False.
# __le__(self, other): Магический метод,
# который определяет операцию "меньше или равно" (<=) для двух прямоугольников.
# Принимает другой прямоугольник other.
# Возвращает True, если площадь первого прямоугольника
# меньше или равна площади второго, иначе False.
# __str__(self): Магический метод,
# возвращающий строковое представление прямоугольника.
# Возвращает строку, описывающую ширину и высоту прямоугольника в виде:
# Прямоугольник со сторонами 2 и 3,
# где первое число - это ширина, а второе - высота.
# __repr__(self): Магический метод,
# возвращающий строковое представление прямоугольника,
# которое может быть использовано для создания
# нового объекта такого же класса с теми же атрибутами.
# Пояснение:
# Метод __add__ объединяет два прямоугольника по периметру
# и создает новый прямоугольник.
# Метод __sub__ вычитает один прямоугольник из другого,
# представляя разницу периметров исходных прямоугольников,
# и создает новый прямоугольник.
# Методы сравнения __lt__, __eq__ и __le__
# сравнивают прямоугольники по их площади.
# Методы __str__ и __repr__ предоставляют
# строковое представление объекта класса Rectangle.
# Пример использования:
# На входе:
# rect1 = Rectangle(5, 10)
# rect2 = Rectangle(3, 7)
# print(f"Периметр rect1: {rect1.perimeter()}")
# print(f"Площадь rect2: {rect2.area()}")
# print(f"rect1 < rect2: {rect1 < rect2}")
# print(f"rect1 == rect2: {rect1 == rect2}")
# print(f"rect1 <= rect2: {rect1 <= rect2}")
# rect3 = rect1 + rect2
# print(f"Периметр rect3: {rect3.perimeter()}")
# rect4 = rect1 - rect2
# print(f"Ширина rect4: {rect4.width}")
# На выходе:
# Периметр rect1: 30
# Площадь rect2: 21
# rect1 < rect2: False
# rect1 == rect2: False
# rect1 <= rect2: False
# Периметр rect3: 50
# Ширина rect4: 2


class Rectangle:

    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.width, self.height = args[0], args[0]
        elif len(args) == 2:
            self.width, self.height = args
        else:
            raise ValueError

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def __add__(self, other: "Rectangle"):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __sub__(self, other: "Rectangle"):
        new_width = abs(self.width - other.width)
        new_height = abs(self.height - other.height)
        return Rectangle(new_width, new_height)

    def __eq__(self, other: "Rectangle") -> bool:
        return self.area() == other.area()

    def __lt__(self, other: "Rectangle") -> bool:
        return self.area() < other.area()

    def __le__(self, other: "Rectangle") -> bool:
        return self.area() <= other.area()

    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self.width} и {self.height}'

    def __repr__(self) -> str:
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
