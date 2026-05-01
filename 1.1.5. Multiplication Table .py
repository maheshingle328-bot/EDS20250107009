"""Write a Python program that takes an integer as input and prints the multiplication table for that integer from 1 to 10.



Input Format:

The first line of input contains an integer that represents the number for which the multiplication table is to be printed.


Output Format:

Print the multiplication table for the given number in the format:
<number> x <multiplier> = <result>


Note:

The character "x" is used in the output to represent multiplication.
Refer to the visible test-cases for more clarity.
"""
#write your code here...
n=int(input())
for i in range(1,11):
	print(f"{n} x {i} = {n*i}",end="\n")