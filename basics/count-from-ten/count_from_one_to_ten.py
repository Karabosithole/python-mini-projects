# Using a for loop
for i in range(1, 11):
    print(f"{i},", end=' ')
print()

# Using a while loop
i = 1
while i <= 10:
    print(f"{i},", end=' ')
    i += 1
print()

# Using a list comprehension
print(", ".join([str(i) for i in range(1, 11)]))

# Using recursion
def count_up(n=1):
    if n > 10:
        return
    print(f"{n},", end=' ')
    count_up(n + 1)

count_up()
print()

# Using a generator
def count_generator():
    for i in range(1, 11):
        yield i

print(", ".join([str(i) for i in count_generator()]))
