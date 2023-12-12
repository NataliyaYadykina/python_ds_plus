# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters
import unittest


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


class TestClearText(unittest.TestCase):

    def test_no_changes(self):
        self.assertEqual(clear_text('hello world'), 'hello world',
                         msg='Не должно быть изменений')

    def test_change_register(self):
        self.assertEqual(clear_text('HELLO world'), 'hello world',
                         msg='Регистр должен быть в lower')

    def test_delete_punctuation(self):
        self.assertEqual(clear_text('hello,,, world!!!'), 'hello world',
                         msg='Знаки пунктуации должны быть удалены')

    def test_foreign_alphabet(self):
        self.assertEqual(clear_text('hello мир'), 'hello ',
                         msg='Символы другого алфавита должны удалиться')

    def test_all_rules(self):
        self.assertEqual(clear_text('Hello,,, мир!!'), 'hello ',
                         msg='Должны соблюстись все правила очистки.')


if __name__ == "__main__":
    unittest.main(verbosity=4)
