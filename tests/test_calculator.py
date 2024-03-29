from decimal import Decimal
import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(2, 3) == Decimal('5')

def test_subtract(calculator):
    assert calculator.subtract(5, 2) == Decimal('3')

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == Decimal('6')

def test_divide(calculator):
    assert calculator.divide(6, 3) == Decimal('2')

def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)

def test_unknown_operation(calculator):
    with pytest.raises(AttributeError):
        calculator.power(2, 3)  # power operation is not defined in Calculator
