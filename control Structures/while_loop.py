# 1. Print numbers 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Print the square of numbers 1 to 5
i = 1
while i <= 5:
    print(f"Square of {i}: {i ** 2}")
    i += 1

# 3. Keep asking for a password until the correct one is entered
password = "secret"
attempt = ""
while attempt != password:
    attempt = input("Enter the password: ")
print("Access granted!")

# 4. Print all odd numbers from 1 to 20
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

# 5. Calculate the sum of numbers from 1 to 10
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print(f"Total sum: {total}")

# 6. Infinite loop with a break condition
while True:
    response = input("Type 'exit' to quit: ")
    if response.lower() == "exit":
        break

# 7. Print each character in a string
word = "Python"
i = 0
while i < len(word):
    print(word[i])
    i += 1

# 8. Countdown from 10 to 1
i = 10
while i > 0:
    print(i)
    i -= 1

# 9. Skip printing the number 5
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1

# 10. Loop through a list using an index
numbers = [10, 20, 30, 40, 50]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
