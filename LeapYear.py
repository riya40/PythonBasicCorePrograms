"""
Determining the given Year is Leap Or Not
"""

year = int(input("enter the year"))
if (year % 4 == 0) and (year % 100 != 0):
    print(year, "leap year")
else:
    print(year, "not leap year")
