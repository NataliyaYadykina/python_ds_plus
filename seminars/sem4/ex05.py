# Задание №5
# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


def get_bonuses_dict(names: list[str],
                     salaries: list[int | int],
                     bonuses: list[str]):
    bonus_dict = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        bonus_dict[name] = salary * float(bonus[:-1]) / 100
    return bonus_dict


print(get_bonuses_dict(["Иван", "Николай", "Пётр", "Харитон"],
                       [125_000, 96_000, 109_000, 100_000],
                       ['10%', '25.5%', '13.3%', '42.73%']))
