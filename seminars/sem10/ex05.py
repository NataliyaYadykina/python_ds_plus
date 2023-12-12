# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Animal:

    def __init__(self, name, age, legs_count, *args, **kwargs) -> None:
        self.name = name
        self.age = age
        self.legs_count = legs_count
        self.additional_info = [args, kwargs]

    def birthday(self):
        self.age += 1

    def full_name(self):
        return self.name


class Lama(Animal):

    def __init__(self, name, age, legs_count, spec_range) -> None:
        super().__init__(name, age, legs_count)
        self.area = spec_range

    def show_info(self):
        return (self.name, self.age, self.legs_count, self.area)


class Penguin(Animal):

    def __init__(self, name, age,
                 legs_amount, wings_count,
                 bill_length, bill_depth, color):
        super().__init__(name, age, legs_amount)
        self.wings_count = wings_count
        self.bill_length = bill_length
        self.bill_depth = bill_depth
        self.color = color

    def birthday(self):
        self.age += 7

    def bill_category(self):
        if self.bill_length > 10 and self.bill_depth > 3:
            return "Big"
        return "Average"


class Wolf(Animal):

    def __init__(self, name, age, legs_amount, speed, color,):
        super().__init__(name, age, legs_amount)
        self.speed = speed
        self.color = color

    def time_for_distance(self, distance):
        return distance/self.speed

    def survival(self, season):
        if self.color == "white" and season == "winter":
            return "great"
        elif self.color == "gray" and season in ["summer", "spring", "autumn"]:
            return "great"
        else:
            return "terrible"


if __name__ == "__main__":

    lama = Lama('Lama', 20, 4, 'South America')
    lama.birthday()
    print(lama.full_name())
    print(lama.show_info())

    p1 = Penguin("Randy", 1, 2, 2, 11, 4, "White")
    p2 = Penguin("Richard", 2, 2, 2, 7, 2, "White")
    p1.birthday()
    p2.birthday()
    print(p1.full_name(), p2.full_name())
    print(p1.bill_category(), p2.bill_category())
    print(p1.age, p2.age)

    w1 = Wolf("Polkan", 3, 4, 60, "gray")
    w2 = Wolf("Akela", 13, 4, 67, "white")
    w1.birthday()
    w2.birthday()
    print(w1.full_name(), w2.full_name())
    print(w1.survival('autumn'), w2.survival('winter'))
    print(w1.age, w2.age)

    animal = Animal("Polkan", 3, 4, 60, "gray")
    animal.birthday()
    print(animal.full_name(), animal.age)
    print(animal.additional_info)
