# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


class FactorialGeneration:

    def __init__(self, *args) -> None:
        match len(args):
            case 1:
                self.stop = args[0]
                self.start = 1
                self.step = 1
            case 2:
                self.start, self.stop = args
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop + 1:
            result = 1
            for i in range(1, self.start + 1):
                result *= i
            self.start += self.step
            return result
        raise StopIteration


if __name__ == "__main__":
    factorial1 = FactorialGeneration(3)
    for i in factorial1:
        print(i)

    print()

    factorial2 = FactorialGeneration(1, 4, 1)
    for i in factorial2:
        print(i)

    print()

    factorial4 = FactorialGeneration(1, 6, 2)
    for i in factorial4:
        print(i)

    print()

    factorial3 = FactorialGeneration(1, 3)
    for i in factorial3:
        print(i)
