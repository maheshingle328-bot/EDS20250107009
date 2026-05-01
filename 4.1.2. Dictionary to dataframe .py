""" dictionary of lists has been provided to you in the editor. Create a DataFrame from the dictionary of lists and perform the listed operations, then display the DataFrame before and after each manipulation.



Create the DataFrame:

Convert the dictionary to a Pandas DataFrame.


Add a new row:

Take inputs from the user for the new row data (name, age).
Add the new row to the DataFrame.
Display the DataFrame after adding the new row.


Modify a row:

Modify a specific row by changing the age. Take the row index and new age value from the user.
Display the DataFrame after modifying the row.


Delete a row:

Take the row index to be deleted from the user.
Remove the specified row.
Display the DataFrame after deleting the row.


Add a new column:

Add a column Gender with values taken from the user.
Display the DataFrame after adding the new column.


Modify a column:

Convert names to uppercase.
Display the DataFrame after modifying the column.


Delete a column:

Remove the Age column.
Display the DataFrame after deleting the column.
"""
import pandas as pd

# Provided dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Adding a new row
name = input("New name: ")
age = int(input("New age: "))

df.loc[len(df)] = [name, age]


# Display the DataFrame after adding a new row
print("After adding a row:\n",df)
index = int(input("Index of row to modify: "))
new_age = int(input("New age: "))

df.loc[index, 'Age'] = new_age

# Modifying a row


# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)
del_index = int(input("Index of row to delete: "))
# Deleting a row
df=df.drop(del_index).reset_index(drop=True)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

genders=input("Enter genders separated by space: ").split()
df["Gender"]=genders
# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df['Name']=df['Name'].str.upper()
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df=df.drop('Age',axis=1)
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
