"""
A simple calculator module with basic arithmetic operations and input validation.
"""

MAX_VALUE = 1_000_000
MIN_VALUE = -1_000_000


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def _validate_values(self, *values):
        """Validate that all values are within the allowed range."""
        for v in values:
            if v < MIN_VALUE or v > MAX_VALUE:
                raise InvalidInputException(
                    f"Input value {v} is outside valid range "
                    f"[{MIN_VALUE}, {MAX_VALUE}]"
                )

    def add(self, a, b):
        """Add two numbers."""
        self._validate_values(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        self._validate_values(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        self._validate_values(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        self._validate_values(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
