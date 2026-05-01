""""ou are given two arrays arr1 and arr2. You need to perform horizontal and vertical stacking operations on them using NumPy.

Horizontal Stacking: Stack the two matrices horizontally (side by side).
Vertical Stacking: Stack the two matrices vertically (one below the other).


Input Format:

The program should first prompt the user to input two 3x3 arrays.
Each array consists of 3 rows, and each row contains 3 space-separated integers.
The user will input the two arrays row by row.


Output Format:

The program should display the result of the Horizontal Stack (side-by-side stacking) of the two arrays.
The program should then display the result of the Vertical Stack (one below the other) of the two arrays."""
import numpy as np

# Input matrices
print("Enter Array1:")
arr1 = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Array2:")
arr2 = np.array([list(map(int, input().split())) for i in range(3)])

# Perform horizontal stacking (hstack)
print("Horizontal Stack:")
print(np.hstack((arr1, arr2)))

# Perform vertical stacking (vstack)
print("Vertical Stack:")
print(np.vstack((arr1, arr2)))