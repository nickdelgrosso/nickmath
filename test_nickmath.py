import pytest
from nickmath import multiply

@pytest.fixture
def data():
    a = 3
    return a


def test_multiply_data(data):
    assert multiply(data, 3) == 9


def test_multiply_positive():
    z = multiply(3, 4)
    assert z == 12


def test_multiply_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative():
    assert multiply(5, -4) == -20
    assert multiply(-4, 5) == -20
    assert multiply(-3, -3) == 9



# def test_multiply_float():
#     z = multiply(3, 4.5)
#     assert z == 13.5