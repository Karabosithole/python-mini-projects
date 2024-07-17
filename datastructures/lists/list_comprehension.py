# 1. Iterate through the list and print elements
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. Iterate through the list with indices
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# 3. Iterate through a list using a while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


"""SLICING"""

# 1. Get a sublist
numbers = [10, 20, 30, 40, 50]
print("Sublist (first 3 elements):", numbers[:3])

# 2. Reverse a list using slicing
print("Reversed list:", numbers[::-1])

# 3. Slice with a step
print("Every second element:", numbers[::2])


"""Advanced Operations"""

# 1. List comprehension to square each element
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print("Squared numbers:", squared)

# 2. Filter even numbers using list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# 3. Combine two lists using zip
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
combined = list(zip(list1, list2))
print("Combined list:", combined)

# 4. Flatten a list of lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened)


