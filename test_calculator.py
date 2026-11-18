import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    assert calc.add(10, 5) == 15


def test_subtraction(calc):
    assert calc.subtract(10, 5) == 5


def test_multiplication(calc):
    assert calc.multiply(10, 5) == 50


def test_division(calc):
    assert calc.divide(10, 5) == 2


def test_division_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)


def test_negative_numbers(calc):
    assert calc.add(-10, 5) == -5


def test_zero_addition(calc):
    assert calc.add(10, 0) == 10


def test_decimal_division(calc):
    assert calc.divide(5, 2) == 2.5