# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def my_get(my_dict: dict, key, default_val=None):
    try:
        return my_dict[key]
    except KeyError:
        return default_val


if __name__ == "__main__":
    d_dict = {1: '1', 2: '2', 3: '3'}
    print(my_get(d_dict, 2))
    print(my_get(d_dict, 4, 'Not found'))
    print(my_get(d_dict, 1, 'Not found'))
