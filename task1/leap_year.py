'''Extended Leap Year Task — Given a year, return True if it is a leap year, otherwise return False, following the Gregorian
calendar rules:
• The year can be evenly divided by 4 → Leap year, unless:
• The year can be evenly divided by 100 → NOT a leap year, unless:
• The year is also evenly divisible by 400 → IS a leap year
Note: Years 2000, 2400 are leap years. Years 1800, 1900, 2100, 2200, 2300, 2500 are NOT leap years.
'''

year=input("enter the years : ")
leap=False

if year % 4==0:
    if year%100==0:
        if year%400==0:
            leap=True
        else:
            leap=False
    else:
        leap=True
else:
    leap=False

print(leap)