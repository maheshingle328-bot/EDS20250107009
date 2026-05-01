"""Write a Python program that takes the file name of a CSV file containing student details, including roll numbers and their marks in three subjects as input, reads the data, and performs the following operations:

Print all student details: Display the complete details of all students, including roll numbers and marks for all subjects.
Find total students: Determine the total number of students in the dataset.
Print all student roll numbers: Extract and print the roll numbers of all students.
Print Subject 1 marks: Extract and print the marks of all students in Subject 1.
Find minimum marks in Subject 2: Identify the lowest marks in Subject 2.
Find maximum marks in Subject 3: Identify the highest marks in Subject 3.
Print all subject marks: Display the marks of all students for each subject.
Find total marks of students: Compute the total marks for each student across all subjects.
Find the average marks of each student: Compute the average marks for each student.
Find average marks of each subject: Compute the average marks for all students in each subject.
Find average marks of Subject 1 and Subject 2: Compute the average marks for Subject 1 and Subject 2.
Find average marks of Subject 1 and Subject 3: Compute the average marks for Subject 1 and Subject 3.
Find the roll number of the student with maximum marks in Subject 3: Identify the student with the highest marks in Subject 3 and print their roll number.
Find the roll number of the student with minimum marks in Subject 2: Identify the student with the lowest marks in Subject 2 and print their roll number.
Find the roll number of students who scored 24 marks in Subject 2: Identify students who obtained exactly 24 marks in Subject 2 and print their roll numbers.
Find the count of students who got less than 40 marks in Subject 1: Count the number of students who scored less than 40 marks in Subject 1.
Find the count of students who got more than 90 marks in Subject 2: Count the number of students who scored more than 90 marks in Subject 2.
Find the count of students who scored >=90 in each subject: Count the number of students who scored 90 or more marks in each subject.
Find the count of subjects in which each student scored >=90: Determine how many subjects each student scored 90 or more marks in.
Print Subject 1 marks in ascending order: Sort and print the marks of students in Subject 1 in ascending order.
Print students who scored between 50 and 90 in Subject 1: Display students who scored marks between 50 and 90 in Subject 1.
Find index positions of students who scored 79 in Subject 1: Identify the index positions of students who scored exactly 79 marks in Subject 1.


Note: Fill in the missing code to perform the above-mentioned operations."""
import numpy as np
import pandas as pd
a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)


# 1. Print all student details
print("All student Details:\n",a  )

# 2. print total students

print("Total Students:",a.shape[0] )

# 3. Print all student Roll numbers
print("All Student Roll Nos", a[:, 0]   )

# 4. Print subject 1 marks
print("Subject 1 Marks",a[:, 1] )

# 5. print minimum marks of Subject 2
print("Min marks in Subject 2", np.min(a[:, 2])     )

# 6. print maximum marks of Subject 3
print("Max marks in Subject 3", np.max(a[:, 3])    )

# 7. Print All subject marks
print("All subject marks:", a[:, 1:]      )

# 8. print Total marks of students
print("Total Marks", np.sum(a[:, 1:],axis = 1)       )

# 9. print average marks of each student
print(np.round(np.mean(a[:, 1:],axis = 1), 1))

# 10. print average marks of each subject
print("Average Marks of each subject",  np.round(np.mean(a[:, 1:], axis = 0), 1)     )

# 11. print average marks of S1 and S2
print("Average Marks of S1 and S2",  np.round(np.mean(a[:, 1:3], axis = 0), 1)     )        

# 12. print average marks of S1 and S3
print("Average Marks of S1 and S3",   np.round(np.mean(a[:, [1, 3]],axis = 0), 1)     )  

# 13. print Roll number who got maximum marks in Subject 3

print("Roll no who got maximum marks in Subject 3",   a[np.argmax(a[:, 3]), 0]        )

# 14. print Roll number who got minimum marks in Subject 2

print("Roll no who got minimum marks in Subject 2", a[np.argmin(a[:, 2]), 0]     )

# 15. print Roll number who got 24 marks in Subject 2

print("Roll no who got 24 marks in Subject 2", a[a[:, 2]==24]  [:, [0]]    )

# 16. print count of students who got marks in Subject 1 < 40
print("Count of students who got marks in Subject 1 < 40",  np.sum(a[:, 1] < 40))

# 17. print count of students who got marks in Subject 2 > 90
print("Count of students who got marks in Subject 2 > 90:", np.sum(a[:, 2] > 90)  )

# 18. print count of students in each subject who got marks >= 90
print("Count of students in each subject who got marks >= 90:", np.sum(a[:, 1:] >= 90, axis = 0)         )

# 19. print count of subjects in which each student got marks >= 90
print("Roll no:", a[:, 0]     )
print("Count of subjects in which student got marks >= 90:", np.sum(a[:, 1:] >= 90, axis = 1)      )

# 20. Print S1 marks in ascending order

print(np.sort(a[:, 1] ))

# 21. Print S1 marks >= 50 and <= 90

print(a[(a[:, 1] >= 50 ) & (a[:, 1] <= 90)])
print(a)
# 22. Print the index position of marks 79
print(np.where(a[:, 1] == 79))