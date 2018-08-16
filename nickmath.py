
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

        >>> multiply(5, 0)
        0

        >>> multiply(5, -4)
        -20

        >>> multiply(-4, 5)
        -20
    """
    y_is_negative = y < 0
    x_is_negative = x < 0
    z = sum([abs(x) for _ in range(abs(y))])
    if y_is_negative:
        z *= -1
    if x_is_negative:
        z *= -1
    return z

# print(add(3, y=20) == 23)
# print(multiply(3, 4) == 12)
# print(multiply(4, 0) == 0)
# print(multiply(4, -2) == -8)