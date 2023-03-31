#
# Homework №1.
#   Functions and Data structures.
#


def power_numbers(*integers: int) -> list[int]:
    """Takes N inbound ints and returns a list with the squares of each.

    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]

    """

    return [i**2 for i in integers]


def is_prime(integer: int) -> bool:
    """Checks if inbound int is a prime number and returns {True|False} accordingly.

    >>> is_prime(16)
    False
    >>> is_prime(2)
    True

    """

    if abs(integer) < 2:
        return False

    for divider in range(2, abs(integer)):
        if (integer % divider) == 0:
            return False
    return True


# Const for 'filter_type' parameter - see 'filter_numbers(...)' function below
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(integers_list: list[int], filter_type: str) -> list[int]:
    """Returns the inbound list filtered according to 'filter_type' parameter value.

    'filter_type' values allowed: f{ODD | EVEN | PRIME}.    //"odd", "even" or "prime"//

    >>> filter_numbers([1, 2, 3, 11, 12], ODD)
    [1, 3, 11]
    >>> filter_numbers([1, 2, 3, 11, 12], EVEN)
    [2, 12]
    >>> filter_numbers([1, 2, 3, 11, 12], PRIME)
    [2, 3, 11]

    """

    if filter_type == ODD:
        checker = lambda x: (x % 2) == 1
    elif filter_type == EVEN:
        checker = lambda x: (x % 2) == 0
    elif filter_type == PRIME:
        checker = is_prime
    else:
        raise ValueError(
            f"Wrong 'filter_type' value = \"{filter_type}\" "
            f'(use "{ODD}", "{EVEN}" or "{PRIME}" instead).'
        )

    return list(filter(checker, integers_list))


if __name__ == "__main__":
    print("\nI am a 'homework_01/main.py'")
