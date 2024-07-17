# Using a for loop
for i in range(10, 0, -1):
    print(f"{i},", end=' ')
print()

# Using a while loop
i = 10
while i > 0:
    print(f"{i},", end=' ')
    i -= 1
print()

# Using a list comprehension
print(", ".join([str(i) for i in range(10, 0, -1)]))

# Using recursion
def count_down(n=10):
    if n < 1:
        return
    print(f"{n},", end=' ')
    count_down(n - 1)

count_down()
print()

# Using a generator
def count_down_generator():
    for i in range(10, 0, -1):
        yield i
# printing making sure its in list form
print(", ".join([str(i) for i in count_down_generator()])) 

