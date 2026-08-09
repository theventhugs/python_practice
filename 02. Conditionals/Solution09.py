# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

# getting correct year from the user
while(True):
    try:
        year = int(input("Enter year you want to check: ").strip())
        if year < 1:
            print("Not a valid year: enter year greater than 0")
            continue
        break
    except Exception as ValueError:
        print("Please enter an int value greater than 0")

# the Core logic
"""
if year % 4 == 0:
    if year % 100 != 0:
        print("A leap year")
    elif year % 100 == 0 and year % 400 == 0:
        print("A leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")
"""
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year")
else:
    print(year, "is NOT a leap year")