# Задание №6
# Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах
# отгадывания.
# Для хранения используйте защищённый словарь уровня
# модуля.
# Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
# Для формирования результатов используйте генераторное
# выражение.

__all__ = ['mystery_game']

results_dict = {}


def mystery_game(mystery: str,
                 answers_list: list[str],
                 count: int) -> int:
    print(f'{mystery}')
    for i in range(count):
        user_answer = input('Enter your answer: ')
        if user_answer.lower() in answers_list:
            count = i + 1
            save_results(mystery, count)
            return count
    save_results(mystery, count)
    return 0


def save_results(mystery, count):
    global results_dict
    results_dict[mystery] = count


def show_results():
    global results_dict
    print(results_dict)


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
    show_results()
