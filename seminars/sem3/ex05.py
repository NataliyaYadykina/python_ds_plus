# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_list = [1, 2, 3, 3, 2, 1, 5, 6, 7, 3]
list_result = []

for index, element in enumerate(my_list, 1):
    if element % 2 != 0:
        list_result.append(index)

print(list_result)
