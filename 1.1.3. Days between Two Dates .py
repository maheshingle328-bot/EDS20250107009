"""Write a Python program to calculate number of days between two dates.



Input Format:

The first line contains the first date in the format 
.
The second line contains the second date in the format 
.


Output Format:

An integer representing the number of days between the given dates.


Note:

The first date should always be considered earlier than the second date.est case 1
Test case 1
2014-07-02	
2014-11-02	
123⏎	
Test case 2
2014-07-02	
2014-07-11	
9⏎"""
from datetime import date
d1 = input().strip().split('-')
d2 = input().strip().split('-')
date1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
date2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
print((date2 - date1).days)