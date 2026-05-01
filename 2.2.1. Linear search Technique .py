"""Write a program to check whether the given element is present or not in the array of elements using linear search.



Input format:

The first line of input contains the array of integers which are separated by space
The last line of input contains the key element to be searched


Output format:

If the element is found, print the index.
If the element is not found, print Not found.


Sample Test Case:

Input:

1 2 3 4 3 5 6

3

Output:

2"""
arr=list(map(int,input().split()))
key=int(input())
found=False
for i in range(len(arr)):
	if arr[i]==key:
		print(i)
		found=True
		break
if not found:
	print("Not found")