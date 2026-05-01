"""Write a Python program to print a right-angled triangle pattern of numbers.



Input Format:

The input is an integer, representing the number of rows in the pattern.


Output Format:

The output should display the pattern of numbers separated by space, with each row containing increasing numbers starting from 1 up to the row number.


Note:

Refer to the displayed test cases for the sample pattern."""
n = int(input())
for i in range(1, n + 1):
	for j in range(1, i + 1):
		print(j, end=" ")
	print()