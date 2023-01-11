"""
Домашнее задание №1.
Функции и структуры данных.
"""


def power_numbers(*integers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел:
    
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [i**2 for i in integers]


# filter_ types:
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(integer):
    if abs(integer) < 2:
        return False

    for divider in range(2, abs(integer)):
        if (integer % divider) == 0:
            return False
    return True


def filter_numbers(integers, filter_):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента):

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_ == ODD:
        checker = lambda x: (x % 2) == 1
    elif filter_ == EVEN:
        checker = lambda x: (x % 2) == 0
    elif filter_ == PRIME:
        checker = is_prime
    # else:
    #     raise ValueError("Only {ODD | EVEN | PRIME} is allowed for 'filter_' !!")

    return list(filter(checker, integers))
