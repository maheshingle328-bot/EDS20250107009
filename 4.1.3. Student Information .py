"""Write a program to read a text file containing student information (name, age, and grade) using Pandas. Perform the following tasks:



Display the first five rows of the data frame.
Calculate the average age of the students (limit the average age up to 2 decimal places).
Filter out the students who have a grade above a certain threshold (consider the threshold grade is 'B').


Note:

Refer to the displayed test cases for better understanding."""
import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])

# First five rows
print("First five rows:")
print(data.head())

# Average age (2 decimal places)
avg_age = round(data["Age"].mean(), 2)
print(f"Average age: {avg_age}")

# Filter students with grade up to 'B' (A and B)
filtered_df = data[data["Grade"].isin(["A", "B"])]

print("Students with a grade up to B")
print(filtered_df)

