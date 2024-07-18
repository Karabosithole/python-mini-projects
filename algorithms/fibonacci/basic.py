'''
    Write a function to store the fibonacci sequence upto
    the nth element in a list.
'''

def fibonacci_sequence(n):
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the list with the first two Fibonacci numbers
    fib_list = [0, 1]
    
    # Generate the rest of the sequence
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list

# Example usage:
n = 10
print(f"Fibonacci sequence up to {n} elements: {fibonacci_sequence(n)}")
