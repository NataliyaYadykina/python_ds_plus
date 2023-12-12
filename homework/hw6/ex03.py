# Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты
# и выведите 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте
# подразумевается такая расстановка ферзей на шахматной доске,
# в которой ни один ферзь не бьет другого.
# Другими словами, ферзи размещены таким образом,
# что они не находятся на одной вертикали, горизонтали или диагонали.
# Список из 4х комбинаций координат сохраните в board_list.
# Дополнительно печатать его не надо.
# Пример использования На входе:
# print(generate_boards())
# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)],
#  [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)],
#  [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)],
#  [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]

from random import randint


def is_attacking(q1: tuple, q2: tuple) -> bool:
    return (q1[0] == q2[0]
            or q1[1] == q2[1]
            or (q1[0] == q1[1] and q2[0] == q2[1])
            or (q1[0] == q2[0] + 1 and q1[1] == q2[1] + 1)
            or (q1[0] == q2[0] - 1 and q1[1] == q2[1] - 1))


def check_queens(queens: list[tuple]) -> bool:
    for first_queen in range(len(queens)):
        for second_queen in range(first_queen + 1, len(queens)):
            if is_attacking(queens[first_queen], queens[second_queen]):
                return False
    else:
        return True


def generate_boards():
    board_list = []
    while len(board_list) != 4:
        temp_result = []
        for _ in range(8):
            temp_result.append((randint(1, 8), randint(1, 8)))
        if check_queens(temp_result):
            board_list.append(temp_result)
    return board_list


print(generate_boards())
