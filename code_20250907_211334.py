def subtract_numbers():
    """Subtracts two numbers provided by the user.

    Handles non-numeric input with error messages.
    """
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"The result is: {result}")
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    subtract_numbers()