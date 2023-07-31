## Вывести все нечетные числа больше 50, используя функцию filter().

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def foo(x):
    if x % 2 != 0:
        if x > 50:
            return True
    return False


print(list(filter(foo, numbers)))
