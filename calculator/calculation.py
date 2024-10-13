from typing import List

class Calculation:
    """Represents a single calculation."""
    
    def __init__(self, operation: str, result: float):
        self.operation = operation  # Stores the operation as a string (e.g., "3 + 4")
        self.result = result        # Stores the result of the operation
    
    # Instance method to display the calculation details
    def display(self) -> str:
        return f"Operation: {self.operation}, Result: {self.result}"

class Calculator:
    """A simple calculator that can add, subtract, multiply, and divide and store history."""
    
    _history: List[Calculation] = []  # Class-level list to store calculation history

    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Static method to subtract two numbers."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Static method to multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Static method to divide two numbers. Throws an exception if b is zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return a / b

    @classmethod
    def add_to_history(cls, operation: str, result: float) -> None:
        """Class method to add a calculation to the history."""
        cls._history.append(Calculation(operation, result))

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Class method to retrieve the last calculation in history."""
        if cls._history:
            return cls._history[-1]
        else:
            raise IndexError("No calculations in history.")

    @classmethod
    def clear_history(cls) -> None:
        """Class method to clear all history."""
        cls._history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Class method to return the entire history."""
        return cls._history