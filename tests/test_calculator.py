import pytest
from calculator.calculation import Calculator  # Import from calculation.py

@pytest.fixture
def setup_calculator():
    """Fixture to clear history before each test."""
    Calculator.clear_history()

#commented out to run faker
'''
@pytest.mark.parametrize("a, b, expected", [(3, 4, 7), (-1, 5, 4), (0, 0, 0)])
def test_add(setup_calculator, a, b, expected):
    result = Calculator.add(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(10, 5, 5), (-1, -1, 0), (0, 0, 0)])
def test_subtract(setup_calculator, a, b, expected):
    result = Calculator.subtract(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(3, 3, 9), (-2, 5, -10), (0, 10, 0)])
def test_multiply(setup_calculator, a, b, expected):
    result = Calculator.multiply(a, b)
    assert result == expected

@pytest.mark.parametrize("a, b, expected", [(10, 2, 5), (-10, 5, -2)])
def test_divide(setup_calculator, a, b, expected):
    result = Calculator.divide(a, b)
    assert result == expected
'''
def test_calculator_operations(a, b, operation, expected):
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError):
            operation(a, b)
    else:
        assert operation(a, b) == expected

def test_add_to_history(setup_calculator):
    result = Calculator.add(3, 4)
    Calculator.add_to_history("3 + 4", result)
    last_calc = Calculator.get_last_calculation()
    assert last_calc.operation == "3 + 4"
    assert last_calc.result == 7

def test_clear_history(setup_calculator):
    result = Calculator.add(3, 4)
    Calculator.add_to_history("3 + 4", result)
    Calculator.clear_history()
    with pytest.raises(IndexError):
        Calculator.get_last_calculation()

def test_get_history(setup_calculator):
    result1 = Calculator.add(3, 4)
    Calculator.add_to_history("3 + 4", result1)
    
    result2 = Calculator.subtract(10, 5)
    Calculator.add_to_history("10 - 5", result2)
    
    history = Calculator.get_history()
    assert len(history) == 2
    assert history[0].operation == "3 + 4"
    assert history[1].operation == "10 - 5"