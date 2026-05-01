"""Write a Python program that implements a menu-driven interface for managing a list of integers. The program should have the following menu options:

1. Add

2. Remove

3. Display

4. Quit



The program should repeatedly prompt the user to enter a choice from the menu. Depending on the choice selected, the program should perform the following actions:

Add: Prompts the user to enter an integer and add it to the integer list. If the input is not a valid integer, display "Invalid input".
Remove: Prompts the user to enter an integer to remove from the list. If the integer is found in the list, remove it; otherwise, display "Element not found". If the list is empty, display "List is empty".
Display: Displays the current list of integers. If the list is empty, display "List is empty".
Quit: Exits the program.
The program should handle invalid menu choices by displaying "Invalid choice".Ensure that the program continues to prompt the user until they choose to quit (option 4).

"""
my_list = []   # Create list outside loop

while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")

	n = int(input("Enter choice: "))

	if n == 1:
		integer = int(input("Integer: "))
		my_list.append(integer)
		print("List after adding:", my_list)

	elif n == 2:
		if len(my_list) == 0:
			print("List is empty")
		else:
			val = int(input("Integer: "))
			if val in my_list:
				my_list.remove(val)
				print("List after removing:", my_list)
			else:
				print("Element not found")

	elif n == 3:
		if len(my_list) != 0:
			print( my_list)
		else:
			print("List is empty")

	elif n == 4:
		print()
		break

	else:
		print("Invalid choice")
