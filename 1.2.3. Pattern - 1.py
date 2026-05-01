"""Write a Python program to print a pattern of asterisks in the form of a right-angled triangle.



Input Format:

The input is an integer, representing the number of rows in the pattern.


Output Format

The output should display the pattern of asterisks (*), with each row containing an increasing number of asterisks.


Note: Refer to the displayed test cases for the sample pattern.


"""
n=int(input())
for i in range(1,n+1):
	print("* "*i)