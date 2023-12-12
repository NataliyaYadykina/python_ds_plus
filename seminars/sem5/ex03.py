# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = 'Hello, World!'
result = {i: ord(i) for i in text}
print(result)

res_iter = iter(result.items())
for i in range(5):
    print(next(res_iter))
