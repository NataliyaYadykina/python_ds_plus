# Создайте функцию генератор чисел Фибоначчи fibonacci.
# Пример использования.
# На входе:
# f = fibonacci()
# for i in range(10):
#     print(next(f))
# На выходе:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34


def fibonacci():
    lst = [0, 1]
    n = 0
    while n != 100:
        lst.append(lst[len(lst) - 1] + lst[len(lst) - 2])
        # lst = [lst[1] - lst[0]] + lst
        num = lst[n]
        yield num
        n += 1


f = fibonacci()
for i in range(5):
    print(next(f))
