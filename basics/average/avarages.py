import numpy as np



# List of numbers
numbers = [3, 57, 89, 2, 56, 8, 2]



# Average using a for loop
sum_for = 0
for num in numbers:
    sum_for += num
average_for = sum_for / len(numbers)
print(f"Average using for loop: {average_for}")



# Average using a while loop
sum_while = 0
index = 0
while index < len(numbers):
    sum_while += numbers[index]
    index += 1
average_while = sum_while / len(numbers)
print(f"Average using while loop: {average_while}")



# Average using the statistics library
import statistics
average_statistics = statistics.mean(numbers)
print(f"Average using statistics.mean(): {average_statistics}")



# Average using numpy.average()

average_numpy = np.average(numbers)
print(f"Average using numpy.average(): {average_numpy}")
