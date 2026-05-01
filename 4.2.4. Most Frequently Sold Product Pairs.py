"""Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the following columns: Date, Product, Quantity, Price, and City.
For each date, find all pairs of products that were sold together (i.e., two products sold on the same date).
Output the product pair/s that was sold most frequently.


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
Explanation:

Transactions:

2025-01-01: Product A, Product B
2025-01-02: Product A, Product C
2025-01-03: Product B, Product A
2025-01-04: Product C, Product B
2025-01-05: Product A, Product C
Now, let's count how often the pairs of products appear together:

Product A and Product B: Appear in transactions on 2025-01-01 and 2025-01-03.
Product A and Product C: Appear in transactions on 2025-01-02 and 2025-01-05.
Product B and Product C: Appears in transactions on 2025-01-04.
Most Frequent Product Combinations:

Product A and Product B (2 times)
Product A and Product C (2 times)


Note:

The data cannot be displayed in the file. You can refer to the sample data provided for insights.


"""
import pandas as pd
from itertools import combinations
from collections import Counter

# Prompt user to input the file name
file_name = input()

# Read data from the specified CSV file
df = pd.read_csv(file_name)
# Group products by Date
grouped = df.groupby('Date')['Product'].apply(list)
# Count all product pairs
pair_counter = Counter()

for products in grouped:
	# Generate all unique pairs for the day
	pairs = combinations(sorted(products), 2)
	pair_counter.update(pairs)

# Find the maximum frequency
if pair_counter:
	max_count = max(pair_counter.values())

# Get all pairs with maximum frequency
	most_frequent_pairs = [pair for pair, count in pair_counter.items() if count == max_count]

# Output results
	for pair in most_frequent_pairs:
		print(f"{pair[0]} and {pair[1]}: {max_count} times")
else:
	print("No product pairs found.")
