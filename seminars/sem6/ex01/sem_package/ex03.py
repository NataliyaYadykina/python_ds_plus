# Задание №4
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.

def mystery_game(mystery: str,
                 answers_list: list[str],
                 count: int) -> int:
    print(f'{mystery}')
    for i in range(count):
        user_answer = input('Enter your answer: ')
        if user_answer.lower() in answers_list:
            return i + 1
    return 0


if __name__ == "__main__":
    print(mystery_game("Висит груша. Нельзя скушать",
                       ["лампочка", "лампа"],
                       3))
