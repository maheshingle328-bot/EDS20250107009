"""Write a Python program that accepts an integer 
 as input. Depending on the number of digits in 
.



Constraints:

1 ≤ 
 ≤ 999



Input Format:

The input consists of a single integer 
.


Output Format:

If 
 is a single-digit number, print its square.
If 
 is a two-digit number, print its square root (rounded to two decimal places).
If 
 is a three-digit number, print its cube root (rounded to two decimal places).
Else print "Invalid".Test case 1
9	
81⏎	
Test case 2
166	
5.50⏎	
Test case 3
24	
4.90⏎	
Test case 4
3456	
Invalid⏎"""
n=int(input())
if n>=0 and n<10:
	print(n**2,end="\n")
elif n>=10 and n<100:
	print(f"{n**(1/2):.2f}",end="\n")
elif n>=100 and n<1000:
	print(f"{n**(1/3):.2f}",end="\n")
else:
	print("Invalid",end="\n")