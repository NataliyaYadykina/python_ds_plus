
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.

n = 10
e = 3
sum_numbers = 0

for i in range(0, n + 1, 2):
    if i % e != 0:
        sum_numbers += i

print(sum_numbers)
