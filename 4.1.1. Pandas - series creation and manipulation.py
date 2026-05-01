"""Write a Python program that takes a list of numbers from the user, creates a Pandas series from it, and then calculates the mean of even and odd numbers separately using the groupby and mean() operations.



Hint: You can group the Series based on whether each number is even or odd.



Input Format:

The user should enter a list of numbers separated by space when prompted.

Output Format:

The program should display the mean of even and odd numbers separately.
Each mean value should be displayed with a label indicating whether it corresponds to even or odd numbers.


Refer to the sample test cases for better understanding regarding input and output format."""
import pandas as pd

# Take inputs from the user to create a list of numbers
numbers = list(map(int, input().split()))
s=pd.Series(numbers)
# Create a Pandas series from the list of numbers

# Grouping by even and odd numbers and calculating the mean
grouped =s.groupby(s%2==0).mean()

# Display the mean of even and odd numbers with labels
grouped.index = ['Even' if is_even else 'Odd' for is_even in grouped.index]
print("Mean of even and odd numbers:")
print(grouped)
