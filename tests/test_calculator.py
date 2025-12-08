"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import (
    Calculator,
    InvalidInputException,
)

MAX = 1_000_000
MIN = -1_000_000


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        calc = Calculator()
        a = -5
        b = -3
        expected = -8
        result = calc.add(a, b)
        assert result == expected

    def test_add_positive_and_negative(self):
        calc = Calculator()
        a = 5
        b = -3
        expected = 2
        result = calc.add(a, b)
        assert result == expected

    def test_add_negative_and_positive(self):
        calc = Calculator()
        a = -5
        b = 3
        expected = -2
        result = calc.add(a, b)
        assert result == expected

    def test_add_positive_with_zero(self):
        calc = Calculator()
        a = 5
        b = 0
        expected = 5
        result = calc.add(a, b)
        assert result == expected

    def test_add_zero_with_positive(self):
        calc = Calculator()
        a = 0
        b = 5
        expected = 5
        result = calc.add(a, b)
        assert result == expected

    def test_add_floats(self):
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2
        result = calc.add(a, b)
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        calc = Calculator()
        a = 10
        b = 3
        expected = 7
        result = calc.subtract(a, b)
        assert result == expected

    def test_subtract_negative_numbers(self):
        calc = Calculator()
        a = -10
        b = -3
        expected = -7
        result = calc.subtract(a, b)
        assert result == expected

    def test_subtract_with_zero(self):
        calc = Calculator()
        a = 10
        b = 0
        expected = 10
        result = calc.subtract(a, b)
        assert result == expected
    
    


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        calc = Calculator()
        a = 4
        b = 5
        expected = 20
        result = calc.multiply(a, b)
        assert result == expected

    def test_multiply_negative_and_positive(self):
        calc = Calculator()
        a = -4
        b = 5
        expected = -20
        result = calc.multiply(a, b)
        assert result == expected

    def test_multiply_by_zero(self):
        calc = Calculator()
        a = 123
        b = 0
        expected = 0
        result = calc.multiply(a, b)
        assert result == expected
    
    def test_multiply_more_cases(self):
        calc = Calculator()
        assert calc.multiply(2, 3) == 6
        assert calc.multiply(-2, -3) == 6
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(2, -3) == -6

    


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        calc = Calculator()
        a = 10
        b = 2
        expected = 5.0
        result = calc.divide(a, b)
        assert result == pytest.approx(expected)

    def test_divide_negative_and_positive(self):
        calc = Calculator()
        a = -10
        b = 2
        expected = -5.0
        result = calc.divide(a, b)
        assert result == pytest.approx(expected)

    def test_divide_by_zero_raises(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(10, 0)

    def test_divide_more_cases(self):
        calc = Calculator()
        assert calc.divide(3, 2) == pytest.approx(1.5)
        assert calc.divide(-3, 2) == pytest.approx(-1.5)
        assert calc.divide(-3, -2) == pytest.approx(1.5)
        assert calc.divide(0, 5) == 0



class TestInputValidation:
    """Tests for input range validation."""

    def test_add_raises_when_too_large_first_arg(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(MAX + 1, 0)

    def test_add_raises_when_too_large_second_arg(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, MAX + 1)

    def test_add_raises_when_too_small_first_arg(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(MIN - 1, 0)

    def test_add_raises_when_too_small_second_arg(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, MIN - 1)

    def test_add_accepts_boundary_values(self):
        calc = Calculator()
        result = calc.add(MAX, MIN)
        assert result == MAX + MIN

    def test_subtract_raises_when_too_large(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(MAX + 1, 0)

    def test_subtract_raises_when_too_small(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(MIN - 1, 0)

    def test_multiply_raises_when_too_large(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(MAX + 1, 1)

    def test_multiply_raises_when_too_small(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(MIN - 1, 1)

    def test_divide_raises_when_too_large(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(MAX + 1, 1)

    def test_divide_raises_when_too_small(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(MIN - 1, 1)

    def test_validate_values_checks_each_argument(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc._validate_values(0, MAX + 1)
