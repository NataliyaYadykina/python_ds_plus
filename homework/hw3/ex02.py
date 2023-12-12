# В большой текстовой строке text подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
# (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# Пример
# На входе:
# text = 'Hello world. Hello Python. Hello again.'
# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

text = "Python 3.9 is the latest version of Python. It's awesome!"
count_repeated = 3

result = []
replaced_symbols = ",'-_(){[]}<>$@\"|/*+=?!.;:"

for i in replaced_symbols:
    if i in text:
        text = text.replace(i, " ")

text_list = text.lower().split()

dict_words = {}

for i in text_list:
    if not i.isdigit():
        dict_words[i] = dict_words.get(i, 0) + 1

# print(dict_words)

dict_words = {
    k: dict_words[k] for k in sorted(
        dict_words, key=dict_words.get, reverse=True)}
# print(dict_words)

print(list(dict_words.items())[:count_repeated])
