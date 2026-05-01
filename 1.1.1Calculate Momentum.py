"""Write a program that accepts the mass of an object (in kilograms) and its velocity (in meters per second), then calculates and displays the momentum of the object. The momentum 
 is calculated using the formula:


where:

 is the mass of the object (in kilograms).

 is the velocity of the object (in meters per second).



Input Format:

A single floating-point number representing the mass of the object in kilograms.
A single floating-point number representing the velocity of the object in meters per second.


Output Format:

The output will display calculated momentum with appropriate units (kgm/s) (rounded up to 2 decimal places).

Sample Test Cases
Test case 1
5.0	
10.0	
50.00kgm/s⏎	
Test case 2
2.3	
4.8	
11.04kgm/s⏎	

 is calculated using the formula:


where:

 is the mass of the object (in kilograms).

 is the velocity of the object (in meters per second).



Input Format:

A single floating-point number representing the mass of the object in kilograms.
A single floating-point number representing the velocity of the object in meters per second.


Output Format:

The output will display calculated momentum with appropriate units (kgm/s) (rounded up to 2 decimal places).

Sample Test Cases
Test case 1
5.0	
10.0	
50.00kgm/s⏎	
Test case 2
2.3	
4.8	
11.04kgm/s⏎	"""
m=float(input())
v=float(input())
mom=m*v
print(f"{mom:.2f}",end="kgm/s\n")