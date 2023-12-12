# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

user_str = '-5.2'

for i in user_str:
    if i.isalpha():
        if user_str != user_str.lower():
            print('There is big char', user_str.lower())
        else:
            print('Other cases', user_str.upper())
        break
else:
    if user_str.isdecimal():
        print('int', int(user_str))
    elif '.' in user_str:
        left_str, right_str = user_str.split('.')
        if left_str[-1].isdigit() and right_str.isdigit():
            print('float', float(user_str))
