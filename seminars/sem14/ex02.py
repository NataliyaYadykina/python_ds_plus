# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters


LETTERS = ascii_letters + ' '


def clear_text(text: str) -> str:
    """
    >>> clear_text('hello world')
    'hello world'
    >>> clear_text('HELLO  world')
    'hello  world'
    >>> clear_text('hello,,, world!!!')
    'hello world'
    >>> clear_text('hello мир')
    'hello '
    >>> clear_text('Hello,,, мир!!')
    'hello '
    """
    return (''.join(letter
                    for letter in text
                    if letter in LETTERS)).lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print(clear_text('Hello world!'))
