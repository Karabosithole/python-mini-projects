def fibonacci_recursive(n):
    """
    Recursively calculate the nth Fibonacci number.
    
    :param n: The position in the Fibonacci sequence (1-based index).
    :return: The nth Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_sequence_recursive(n):
    """
    Generate the Fibonacci sequence up to the nth element using recursion.
    
    :param n: Number of elements in the sequence (must be a positive integer).
    :return: List containing the Fibonacci sequence up to the nth element.
    """
    if n <= 0:
        return []
    return [fibonacci_recursive(i) for i in range(1, n + 1)]

# Example usage:
n = 10
print(f"Fibonacci sequence up to {n} elements: {fibonacci_sequence_recursive(n)}")
