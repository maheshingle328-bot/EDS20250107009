"""Write a Python program that takes the following inputs from the user:

Start value: The starting point of the sequence.
Stop value: The sequence should end before this value.
Step value: The increment between each number in the sequence.
The program should then generate a sequence using numpy based on these inputs and print the generated sequence.



Input Format:

The user will input three integer values: start, stop, and step, each on a new line.


Output Format:

The program should print the generated sequence based on the input values."""
import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

# Generate the sequence using np.arange()
arr=np.arange(start,stop,step)
# Print the generated sequence
print(arr)