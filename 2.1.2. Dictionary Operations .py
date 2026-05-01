"""Write a Python program to perform insertion, update, deletion, and traversal operations on a dictionary. An initial dictionary containing 10 predefined records is already given in the program.



Operations to be Performed:

Insertion – Insert a new key-value pair into the dictionary using user input.
Update – Update the value of an existing key using user input.
Deletion – Delete a specified key from the dictionary using user input.
Traversal – Traverse the final dictionary and display all key-value pairs.

Input and Output Format:

Read an integer representing the key to be inserted and a string representing its value. Insert this new key-value pair into the dictionary and display the dictionary after insertion.
Read an integer representing the key to be updated and a string representing the new value. Update the value of the specified key (only if it exists) and display the dictionary after the update.
Read an integer representing the key to be deleted. Delete the specified key from the dictionary (only if it exists) and display the dictionary after deletion.
Finally, traverse the dictionary and display all key-value pairs.
The program should also display the original dictionary before performing any operations. Each output should be printed with appropriate messages.



Note:

All operations must be performed using dictionary methods.
Perform deletion only if possible; leave the dictionary unchanged.
Refer to the visible test cases for better understanding and strictly match with the input/outputs."""
# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}
# Display original dictionary
print("Original Dictionary:", student)

# Insertion
key = int(input())
value = input()
student[key] = value
print("After Insertion:", student)

# Update
update_key = int(input())
update_value = input()

if update_key in student:
    student.update({update_key: update_value})

print("After Update:", student)

# Deletion
delete_key = int(input())

if delete_key in student:
    student.pop(delete_key)

print("After Deletion:", student)

# Traversal
print("Traversing Dictionary:")
for k, v in student.items():
    print(k, ":", v)



