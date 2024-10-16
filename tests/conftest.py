import pytest
from calculator.calculation import Calculator

@pytest.fixture
def calculator():
    """Fixture for creating a Calculator instance for testing."""
    return Calculator()
