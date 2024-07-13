import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

matrix_addition = np.add(matrix1, matrix2)

matrix_multiplication = np.dot(matrix1, matrix2)

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)
print("\nMatrix Addition:")
print(matrix_addition)
print("\nMatrix Multiplication:")
print(matrix_multiplication)
