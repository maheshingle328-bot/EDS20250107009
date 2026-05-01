"""Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the columns: Date, Product, Quantity, Price, and City.
Group the data by Month and calculate the total sales for each month.
Find the month with the highest total sales and display it.
Also, display the total sales for the best month.


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


Note:

The data cannot be displayed in the file. You can refer to the sample data provided for insights.

"""
import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)
#convert Date coloum to datetime
df['Date']=pd.to_datetime(df['Date'])
# Create Month column
df['Month'] = df['Date'].dt.to_period('M')

# Calculate Sales (Quantity * Price)
df['Sales'] = df['Quantity'] * df['Price']

# Group by Month and calculate total sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# Find the month with the highest total sales
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
