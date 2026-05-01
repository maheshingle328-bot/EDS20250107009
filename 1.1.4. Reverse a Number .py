"""Write a Python program to reverse the digits of the number and print the reversed number.



Input Format:

The input is a single integer.


Output Format:

The output prints a single integer, which is the reversed number.
"""
#write your code here...
n=int(input())
str1=str(n)
revnum=str1[::-1]
revnum=int(revnum)
print(revnum,end="\n")