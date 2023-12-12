# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия,
# но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения
# или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн,
# вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


balance = 0
operations_count = 0
BONUS_OPERATIONS_COUNT = 3
PERCENT_FOR_OPERATIONS = 1.03
RICH_LIMIT = 5_000_000
RICH_TAX = 0.9
MIN_NOMINAL = 50
MIN_COMMISSION = 30
MAX_COMMISSION = 600
COMMISION_OUTDRAW = 0.015

while True:
    is_success = False
    if operations_count == BONUS_OPERATIONS_COUNT:
        balance *= PERCENT_FOR_OPERATIONS
        operations_count = 0
    mode = int(input("Введите режим работы (1 - пополнение,\
 2 - снятие, 3 - выход) "))
    if balance > RICH_LIMIT:
        balance *= RICH_TAX
    if mode == 1:
        withdraw = int(input('Введите сумму пополнения: '))
        if withdraw % MIN_NOMINAL == 0:
            balance += withdraw
            is_success = True
    elif mode == 2:
        outdraw = int(input('Введите сумму снятия: '))
        commission = outdraw * COMMISION_OUTDRAW
        if commission < MIN_COMMISSION:
            commission = MIN_COMMISSION
        elif commission > MAX_COMMISSION:
            commission = MAX_COMMISSION

        full_summ = outdraw + commission
        if outdraw % MIN_NOMINAL == 0 and balance > full_summ:
            balance -= full_summ
            is_success = True
    elif mode == 3:
        print('Выход')
        break
    if is_success:
        operations_count += 1
    else:
        print('Сумма некорректна.')

    print(f'Текущий баланс: {balance}')
