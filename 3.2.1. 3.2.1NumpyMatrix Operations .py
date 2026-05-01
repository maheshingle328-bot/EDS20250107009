"""The given code takes two 
 matrices, 
, and 
, as input from the user and converts them into NumPy arrays.



Task:
You are required to compute and display the results of the following matrix operations:

Addition (
)
Subtraction (
)
Element-wise Multiplication (
)
Matrix Multiplication (
)
Transpose of Matrix A

Input Format:

The user will input 3 rows for 
, each containing 3 integers separated by spaces.
Similarly, the user will input 3 rows for 
, each containing 3 integers separated by spaces.

Output Format:

The program should display the results of the operations in the following order:

The result of Addition.
The result of Subtraction.
The result of Element-wise Multiplication.
The result of Matrix Multiplication.
The Transpose of Matrix A.
"""

import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
print("Addition (A + B):")
print(matrix_a+matrix_b)
# Subtraction
print("Subtraction (A - B):")
print(matrix_a-matrix_b)
# Multiplication (element-wise)
print("Element-wise Multiplication (A * B):")
print(matrix_a*matrix_b)
# Matrix multiplication (dot product)
print("A dot B:")
print(matrix_a@matrix_b)
# Transpose
print("Transpose of A:")
print(matrix_a.T)