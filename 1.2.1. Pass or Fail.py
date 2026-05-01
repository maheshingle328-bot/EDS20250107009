"""Write a Python program that accepts the number of courses and the marks of a student in those courses.

The grade is determined based on the aggregate percentage:

If the aggregate percentage is greater than 75, the grade is Distinction.
If the aggregate percentage is greater than or equal to 60 but less than 75, the grade is First Division.
If the aggregate percentage is greater than or equal to 50 but less than 60, the grade is Second Division.
If the aggregate percentage is greater than or equal to 40 but less than 50, the grade is Third Division.


Input Format:

The first input will be an integer 
, the number of courses.
The second input will be 
 integers representing the marks of the student in each of the 
 courses, separated by a space.


Output Format:

If the student passes all courses:

Print the aggregate percentage (formatted to two decimal places).
Print the grade based on the aggregate percentage.
If the student fails any course (marks < 40 in any course), print:

"Fail".


Note:

 Aggregate Percentage: Average performance across all courses, calculated by summing all marks and dividing by the number of courses."""
n = int(input())
marks = list(map(int, input().split()))
fail=False
# Check fail condition
for m in marks:
	if m < 40:
		fail=True
		break
if fail:
	print("Fail")
# If passe
else:
	total = sum(marks)
	percentage = total / n

	print(f"Aggregate Percentage: {percentage:.2f}")

	if percentage >= 75:
		print("Grade: Distinction")
	elif percentage >= 60:
		print("Grade: First Division")
	elif percentage >= 50:
		print("Grade: Second Division")
	else:
		print("Grade: Third Division")