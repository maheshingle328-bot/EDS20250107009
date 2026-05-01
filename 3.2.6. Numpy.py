"""The given code in the editor takes a single array, array1, as space-separated integers as input from the user.

Additionally, it takes the following inputs:

search_value: The value to search for in the array.
count_value: The value to count its occurrences in the array.
broadcast_value: The value to add for broadcasting across the array.


You need to complete the code to perform the following operations:

1. Searching: Find the indices where search_value appears in array1 and print these indices.

2. Counting: Count how many times count_value appears in array1 and print the count.

3. Broadcasting: Add broadcast_value to each element of array1 using broadcasting, and print the resulting array.

4. Sorting: Sort array1 in ascending order and print the sorted array.



Input Format:

A single line containing space-separated integers representing array1.
An integer search_value represents the value to search for in the array.
An integer count_value represents the value to count in the array.
An integer broadcast_value represents the value to add to each element of the array.

Output Format:

The indices where search_value occurs in array1.
The count of occurrences of count_value in array1.
The array after adding the broadcast_value to each element.
The sorted array.
"""
import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))


# 1. Searching (indices)
indices = np.where(array1 == search_value)[0]
print(indices)

# 2. Counting
count = np.count_nonzero(array1 == count_value)
print(count)

# 3. Broadcasting (add value)
broadcasted_array = array1 + broadcast_value
print(broadcasted_array)

# 4. Sorting
sorted_array = np.sort(array1)
print(sorted_array)