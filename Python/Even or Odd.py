# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    """
This function takes a number as input and returns whether it is even or odd.

Args:
    number (int or str): The number to be checked. If a string is provided, it will be converted to an integer.

Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
"""
    if int(number) % 2 == 0:
        # If the number is divisible by 2, it is even and "Even" is returned.
        return ("Even")
    else:
        # If the number is not divisible by 2, it is odd and "Odd" is returned.
        return ("Odd")
