"""Write a Python program that uses recursion to print the first 
 terms of the Fibonacci series.



Input Format:

A single integer 
 representing the number of terms to generate.


Output Format:

A single line containing the first 
 terms of the Fibonacci sequence, separated by spaces.

"""
def fibonacci(n):
	if n<=1:
		return -(n-1)
	else:
		return fibonacci(n-1)+fibonacci(n-2)


n = int(input())
for i in range(1, n + 1):
	print(fibonacci(i), end=" ")
