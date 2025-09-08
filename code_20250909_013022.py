class SimpleCalculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    def add(self, a, b):
        """
        Returns the sum of a and b.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """
        Returns the result of a minus b.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Result of a minus b
        """
        return a - b

    def multiply(self, a, b):
        """
        Returns the product of a and b.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Product of a and b
        """
        return a * b

    def divide(self, a, b):
        """
        Returns the result of a divided by b.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Result of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    """
    Simple command-line interface for the SimpleCalculator.
    """
    calc = SimpleCalculator()

    print("Simple Calculator")
    print("----------------")

    while True:
        try:
            # Get user input
            num1 = float(input("Enter first number (or 'q' to quit): "))
            if num1 == 'q':
                break

            num2 = float(input("Enter second number: "))

            # Choose operation
            print("\nChoose operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            choice = input("Enter choice (1/2/3/4): ")

            # Perform calculation
            if choice == '1':
                result = calc.add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = calc.divide(num1, num2)
                    print(f"\nResult: {num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
            else:
                print("\nInvalid choice. Please try again.")

            print("\n" + "="*30 + "\n")

        except ValueError:
            print("\nInvalid input. Please enter numbers only.\n")
        except KeyboardInterrupt:
            print("\nCalculator exited.")
            break

if __name__ == "__main__":
    main()

# Example usage:
# calc = SimpleCalculator()
# print(calc.add(5, 3))      # Output: 8
# print(calc.subtract(5, 3)) # Output: 2
# print(calc.multiply(5, 3)) # Output: 15
# print(calc.divide(5, 3))    # Output: 1.6666666666666667