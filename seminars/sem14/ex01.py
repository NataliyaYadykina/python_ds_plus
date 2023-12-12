# Задание №1
# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters


LETTERS = ascii_letters + ' '


def clear_text(text: str) -> str:
    return (''.join(letter
                    for letter in text
                    if letter in LETTERS)).lower()


if __name__ == "__main__":
    print(clear_text('Hello world!'))
