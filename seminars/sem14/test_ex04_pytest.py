# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from ex01 import clear_text


def test_no_changes():
    assert clear_text('hello world') == 'hello world'


def test_change_register():
    assert clear_text('HELLO world') == 'hello world'


def test_delete_punctuation():
    assert clear_text('hello,,, world!!!') == 'hello world'


def test_foreign_alphabet():
    assert clear_text('hello мир') == 'hello '


def test_all_rules():
    assert clear_text('Hello,,, мир!!') == 'hello '
