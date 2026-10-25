'''Concepts: Conditional statements, nested if, ternary operator

Write a program that calculates a household electricity bill using slab rates.
REQUIREMENTS
• Accept the number of units consumed. 
• Apply the rates: first 20 units at Rs. 5, next 30 units at Rs. 8, and all remaining units at Rs. 12.
• Add a fixed service charge of Rs. 50 to every bill.
• Use the ternary operator to print "High usage warning" when the total bill exceeds Rs. 1000. 

SAMPLE OUTPUT
Units = 70
Energy charge : Rs. 580
Service charge: Rs. 50
Total bill : Rs. 630'''



units= int(input("enter unit number: "))
service_charge = 50

# Apply the rates: first 20 units at Rs. 5, next 30 units at Rs. 8, and all remaining units at Rs. 12.
if units <= 20:
        print("you have to pay just rs: 5")
        if units <= 30:
            print("you have to pay just rs: 8")
        elif units >= 30:
            print("you have to pay rs: 12")
else :
     print(f'(units)+50')



