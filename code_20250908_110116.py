class Calculator:
    """
    A basic calculator class that performs arithmetic operations.
    """

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers and return the result.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract b from a and return the result.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Difference between a and b
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers and return the result.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Product of a and b
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b and return the result.

        Args:
            a (float): Numerator
            b (float): Denominator

        Returns:
            float: Quotient of a divided by b
        """
        return a / b