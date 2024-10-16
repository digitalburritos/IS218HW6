import pytest
from calculator.calculation import Calculator

def test_add(calculator):
    """Tests the addition operation."""
    assert calculator.add(3, 4) == 7

def test_subtract(calculator):
    """Tests the subtraction operation."""
    assert calculator.subtract(10, 5) == 5

def test_multiply(calculator):
    """Tests the multiplication operation."""
    assert calculator.multiply(3, 4) == 12

def test_divide(calculator):
    """Tests the division operation."""
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero(calculator):
    """Tests division by zero to ensure it raises an exception."""
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
