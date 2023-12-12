# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются
# в одноимённые переменные без s на конце.


def replace_vars_name():
    for name, value in globals().items():
        if name.endswith('s'):
            globals()[name] = None
            globals()[name[:-1]] = value


num = 2
nums = 3
ind = 1
inds = 9

print(globals())
replace_vars_name()
print(globals())
