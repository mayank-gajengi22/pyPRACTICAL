import numpy as np


matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])


addition = matrix1 + matrix2


subtraction = matrix1 - matrix2


multiplication = np.dot(matrix1, matrix2)


division = np.divide(matrix1, matrix2)

print("Matrix Addition:\n", addition)
print("Matrix Subtraction:\n", subtraction)
print("Matrix Multiplication:\n", multiplication)
print("Matrix Division (element-wise):\n", division)
