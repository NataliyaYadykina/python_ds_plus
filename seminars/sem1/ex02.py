# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = 1900
MAIN_CONDITION = 4
EXCEPTION_CONDITION = 100
ADDITIONAL_CONDITION = 100

if (year % MAIN_CONDITION == 0
        and year % EXCEPTION_CONDITION != 0
        or year % ADDITIONAL_CONDITION == 0):
    print('Високосный')
else:
    print('Обычный')
