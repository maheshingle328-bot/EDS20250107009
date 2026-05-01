"""Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the columns: Date, Product, Quantity, Price, and City.
Group the data by City and calculate the total quantity of products sold for each city.
Find the city that sold the most products (based on the total quantity sold).


﻿Sample Data:

Date,Product,Quantity,Price,City
2025-01-01,Product A,5,20,New York
2025-01-01,Product B,3,15,Los Angeles
2025-01-02,Product A,7,20,New York
2025-01-02,Product C,4,30,Chicago
2025-01-03,Product B,2,15,Chicago
2025-01-03,Product A,8,20,Los Angeles
2025-01-04,Product C,6,30,New York
2025-01-04,Product B,5,15,Los Angeles
2025-01-05,Product A,3,20,Chicago
2025-01-05,Product C,10,30,Los Angeles


﻿Note:

The data cannot be displayed in the file. You can refer to the sample data provided for insights."""
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
total_Q_city=df.groupby('City')['Quantity'].sum()
best_city=total_Q_city.idxmax()

# Display the result
print(f"City sold the most products: {best_city}")
