# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (2, 'str', 1.5, True, 5, 7.2, False)
my_dict = {}

for i in my_tuple:
    my_dict[type(i)] = my_dict.get(type(i), [])
    my_dict[type(i)].append(i)

print(my_dict)
