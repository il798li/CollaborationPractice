from __future__ import annotations

class Calculator:
    def multiply(factor1: float, factor2: float) -> float:
        """
        Multiplies two numbers.

        Args:
            factor1 (float): The first factor to multiply.
            factor2 (float): The second factor to multiply.

        Returns:
            float: The product of the two factors.
        """
        return factor1 * factor2

    def divide(dividend: float, divisor: float) -> float:
        """
        Divides two numbers.

        Args:
            dividend (float): The number to divide.
            divisor (float): The number to divide by.

        Returns:
            float: The result of the division.
        """
    
    def add(number1: float, number2: float) -> float:
        """
        Adds two numbers. This one has been done as an example.

        Args:
            number1 (float): The first number to add.
            number2 (float): The second number to add.

        Returns:
            float: The sum of the two numbers.
        """
        return number1 + number2
    
    def subtract(minuend: float, subtrahend: float) -> float:
        """
        Subtracts two numbers.

        Args:
            minuend (float): The number to subtract from.
            subtrahend (float): The number to subtract.

        Returns:
            float: The difference between the two numbers.
        """
    
    def power(base: float, exponent: int) -> float:
        """
        Raises a number to a power. Challenge: Try to use `multiply` to implement this!

        Args:
            base (float): The number to raise.
            exponent (float): The power to raise the number to.

        Returns:
            float: The result of raising the number to the power.
        """

    def add_three_numbers(number1: float, number2: float, number3: float) -> float:
        """
        Adds three numbers.

        Args:
            number1 (float): The first number to add.
            number2 (float): The second number to add.
            number3 (float): The third number to add.

        Returns:
            float: The sum of the three numbers.
        """
        return number1 + number2 + number3

# Don't 
assert Calculator.multiply(2, 3) == 6
assert Calculator.divide(6, 2) == 3
assert Calculator.add(2, 3) == 5
assert Calculator.subtract(5, 2) == 3
assert Calculator.power(2, 3) == 8