import math

pi = 3.14

def add(x, y=2):
    "Returns x + y, or x + 2."
    result = x + y
    return result


def subtract(x, y=2):
    result = x - y
    return result


def multiply(x, y):
    """
    Returns x * y

    Arguments:
        - x (int): the first number to multiply
        - y (int): the second number to multiply

    Returns:
        - z (int): the number x * y

    Examples:
        >>> multiply(4, 5)
        20

    """
    # todo: Deal with floating points when you have time!
    y_is_negative = y < 0
    x_is_negative = x < 0
    z = sum([abs(x) for _ in range(abs(y))])
    if y_is_negative:
        z *= -1
    if x_is_negative:
        z *= -1
    return z


from collections import namedtuple
StatisticResult = namedtuple('StatisticResult', 't p')

def t_test():
    t = 1
    p = .05
    return StatisticResult(t, p)




if __name__ == '__main__':
    print(get_pi())
    print(get_pi())
    print(get_pi())
    print(get_pi())
