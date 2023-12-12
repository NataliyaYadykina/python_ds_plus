# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга
# и check_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину,
# а если бьют - ложь. Не забудьте напечатать результат.
# Пример использования.
# На входе:
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# На выходе:
# False
#   xx  12  13  14  15  16  17  18
#   21  22  23  24  xx  26  27  28
#   31  xx  33  34  35  36  37  38
#   41  42  43  44  45  xx  47  48
#   51  52  xx  57  55  56  57  58
#   61  62  63  64  65  66  xx  68
#   71  72  73  xx  75  76  77  78
#   81  82  83  84  85  86  87  xx

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


def is_attacking(q1: tuple, q2: tuple) -> bool:
    return (q1[0] == q2[0]
            or q1[1] == q2[1]
            or (q1[0] == q1[1] and q2[0] == q2[1])
            or (q1[0] == q2[0] + 1 and q1[1] == q2[1] + 1)
            or (q1[0] == q2[0] - 1 and q1[1] == q2[1] - 1))


def check_queens(queens: list[tuple]) -> bool:
    for first_queen in range(len(queens)):
        # print(queens[first_queen])
        for second_queen in range(first_queen + 1, len(queens)):
            # print(queens[second_queen])
            # print(is_attacking(queens[first_queen], queens[second_queen]))
            if is_attacking(queens[first_queen], queens[second_queen]):
                return False
    else:
        return True


print(check_queens(queens))
