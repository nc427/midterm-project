from decimal import Decimal
from typing import Any
import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return calculator()

def test_add(calculator: Any):
    assert calculator.add(2, 3) == Decimal('5')

def test_subtract(calculator: Any):
    assert calculator.subtract(5, 2) == Decimal('3')

def test_multiply(calculator: Any):
    assert calculator.multiply(2, 3) == Decimal('6')

def test_divide(calculator: Any):
    assert calculator.divide(6, 3) == Decimal('2')

def test_divide_by_zero(calculator: Any):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)

def test_unknown_operation(calculator: Any):
    with pytest.raises(AttributeError):
        calculator.power(2, 3)  # power operation is not defined in Calculator