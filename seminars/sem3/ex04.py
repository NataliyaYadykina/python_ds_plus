# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 3, 2, 1, 5, 6, 7, 3]

for i in my_list:
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)

print(my_list)