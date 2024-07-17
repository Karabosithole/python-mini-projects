def is_even_or_odd(number):
    """
    Determines whether a number is even or odd.

    Parameters:
    number (int): The number to check.

    Returns:
    str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(is_even_or_odd(4))  # Output: "Even"
print(is_even_or_odd(7))  # Output: "Odd"
