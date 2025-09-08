def sum_two_numbers(num1, num2):
    # Check if both arguments are numbers
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError("Both arguments must be numbers")
    
    # Return the sum of the two numbers
    return num1 + num2

# Example of using the function
try:
    result = sum_two_numbers(10, 5)
    print(result)  # Output: 15
    
    # This will raise a TypeError
    # sum_two_numbers(10, '5')
except TypeError as e:
    print(f"Error: {e}")