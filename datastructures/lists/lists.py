"""Python Lists are just like the arrays, declared in other languages which is an ordered collection of data. 
It is very flexible as the items in a list do not need to be of the same type."""

# 1. Create a list of numbers and print it
numbers = [1, 2, 3, 4, 5]
print("List of numbers:", numbers)

# 2. Access list elements using indices
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 3. Modify a list element
numbers[2] = 99
print("Modified list:", numbers)

# 4. Append an element to the list
numbers.append(6)
print("List after appending:", numbers)

# 5. Remove an element from the list
numbers.remove(99)
print("List after removing 99:", numbers)

# 6. Pop the last element
popped = numbers.pop()
print("Popped element:", popped)
print("List after popping:", numbers)

# 7. Insert an element at a specific index
numbers.insert(2, 42)
print("List after inserting 42 at index 2:", numbers)

# 8. Check if an element exists in the list
print("Is 42 in the list?", 42 in numbers)

# 9. Get the length of the list
print("Length of the list:", len(numbers))

# 10. Clear the list
numbers.clear()
print("Cleared list:", numbers)
