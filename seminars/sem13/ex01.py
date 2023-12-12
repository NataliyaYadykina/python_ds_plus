# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.


def correct_num_input() -> int | float:
    while True:
        user_inp = input()
        try:
            if '.' in user_inp:
                return float(user_inp)
            return int(user_inp)
        except ValueError:
            continue


if __name__ == "__main__":
    print(correct_num_input())
