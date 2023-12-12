# Напишите код, который запрашивает число и сообщает
# является ли оно простым или составным.
# Используйте правило для проверки:
# “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(n ** 0.5)
    for odd_i in range(3, sqrt_n + 1, 2):
        if n % odd_i == 0:
            return False

    return True


while True:
    number = int(input('Введите число (до 10^5): '))
    if 2 <= number <= 10 ** 5:
        prime = is_prime(number)
        print(
            f'{number} является {("простым", "составным")[1 - prime]} числом'
            )
        break
    else:
        print('Число должно быть больше 1 и меньше 100000')
