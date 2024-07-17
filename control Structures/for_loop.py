# 1. Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# 2. Print the square of each number in a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f"Square of {num}: {num ** 2}")

# 3. Iterate through a list of names and print a greeting
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")

# 4. Calculate the sum of numbers in a list
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print(f"Total sum: {total}")

# 5. Iterate through a string and print each character
word = "Python"
for char in word:
    print(char)

# 6. Print only the even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 7. Nested loop: Print a multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("----")

# 8. Break statement: Stop printing numbers after 5
for i in range(1, 11):
    if i > 5:
        break
    print(i)

# 9. Continue statement: Skip printing the number 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 10. Loop through a dictionary and print keys and values
fruits = {"apple": 2, "banana": 3, "cherry": 5}
for fruit, count in fruits.items():
    print(f"{fruit}: {count}")
