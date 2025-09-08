def add_numbers(num1: float, num2: float) -> float:
    """
    Adds two numbers and returns the result.

    Args:
        num1 (float): First number to add
        num2 (float): Second number to add

    Returns:
        float: Sum of num1 and num2
    """
    return num1 + num2

def get_number_input(prompt: str) -> float:
    """
    Gets numeric input from user with error handling.

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        float: The valid number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    """
    Main function to run the addition application.
    Gets two numbers from user, adds them, and displays the result.
    """
    print("Simple Addition Application")
    print("---------------------------")

    # Get user input
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")

    # Calculate and display result
    result = add_numbers(num1, num2)
    print(f"\nThe sum of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    # Example usage
    main()