import numpy as np

# 1. Create a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5])

print("1D NumPy Array:")
print(arr)

# 2. Create a 2D NumPy matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D NumPy Matrix:")
print(matrix)

# 3. Create zeros matrix
zeros_matrix = np.zeros((3, 3))

print("\n3x3 Matrix of Zeros:")
print(zeros_matrix)

# 4. Create ones matrix
ones_matrix = np.ones((3, 3))

print("\n3x3 Matrix of Ones:")
print(ones_matrix)

# -----------------------------------
# Array Operations
# -----------------------------------

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Addition
sum_array = arr1 + arr2

print("\nArray Addition:")
print(sum_array)

# Subtraction
diff_array = arr1 - arr2

print("\nArray Subtraction:")
print(diff_array)

# Element-wise multiplication
product_array = arr1 * arr2

print("\nElement-wise Multiplication:")
print(product_array)

# -----------------------------------
# Matrix Multiplication
# -----------------------------------

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

matrix_product = np.dot(matrix1, matrix2)

print("\nMatrix Dot Product:")
print(matrix_product)

# -----------------------------------
# Element-wise Operations
# -----------------------------------

square_array = np.square(arr1)

print("\nElement-wise Square:")
print(square_array)

sqrt_array = np.sqrt(arr1)

print("\nElement-wise Square Root:")
print(sqrt_array)

exp_array = np.exp(arr1)

print("\nElement-wise Exponentiation:")
print(exp_array)

print("\nLab Completed Successfully")
