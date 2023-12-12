# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


def bubble_sort(nums: list[int | float]):
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


numbers = [2, 3, 1, 9, 0, 7]
bubble_sort(numbers)
print(numbers)
