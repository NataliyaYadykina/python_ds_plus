# Задание №5
# Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.


def mystery_game(mystery: str,
                 answers_list: list[str],
                 count: int) -> int:
    print(f'{mystery}')
    for i in range(count):
        user_answer = input('Enter your answer: ')
        if user_answer.lower() in answers_list:
            return i + 1
    return 0


def main():
    mysteries_dict = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    }
    for mystery, answers in mysteries_dict.items():
        print(mystery_game(mystery, answers, 3))


if __name__ == "__main__":
    # print(mystery_game("Висит груша. Нельзя скушать",
    #                    ["лампочка", "лампа"],
    #                    3))
    main()
