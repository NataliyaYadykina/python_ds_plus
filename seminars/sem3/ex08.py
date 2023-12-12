# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {
        'Aaz': ("спички", "спальник", "дрова", "топор"),
        'Skeeve': ("спальник", "спички", "вода", "еда"),
        'Tananda': ("вода", "спички", "косметичка"),
        }

# 1
result_all = None

for name, things in hike.items():
    if result_all is None:
        result_all = set(things)
        continue
    result_all = result_all.intersection(set(things))

print(result_all)

# 2
result_uniq = []

for name, temp_th in hike.items():
    temp_res = set(temp_th)
    all_other = set()
    for things in hike.values():
        if temp_res == set(things):
            continue
        all_other = all_other.union(set(things))
    result_uniq.append((name, temp_res.difference(all_other)))

print(result_uniq)

# 3
result = []
