# Lab 1: Introduction to Python for Machine Learning

print("Hello, welcome to Python for Machine Learning!")

# Variables and basic data types
x = 10
y = 5.5
name = "John"

print(f"Integer value: {x}, Float value: {y}, Name: {name}")

# Arithmetic operation
result = x + y
print(f"Sum of {x} and {y} is {result}")

# List
numbers = [1, 2, 3, 4, 5]
print(f"List of numbers: {numbers}")

# For loop
for number in numbers:
    print(f"Number: {number}")

# If-else condition
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is not greater than {y}")

# Tuple
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")

# Dictionary
my_dict = {"name": "Alice", "age": 25}
print(f"Dictionary: {my_dict}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
