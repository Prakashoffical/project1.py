# Write a Python program to create a simple calculator that takes two numbers (num1 and num2) and an operator (+, −, ×, ÷)
# as input from the user. Perform the corresponding operation based on the given operator using elif statements.


num1 = int(input("Number1:- "))
num2 = int(input("number2:- "))
operator = input("(+, -, *, /):- ")


if operator == "+":
    print( num1 + num2 )
    
elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1*num2)

elif operator == "/":
    print(num1/num2)

else:
    print("invilade operator")

    # it's done