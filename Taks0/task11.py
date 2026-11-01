# Write a program to input a number and determine whether it is positive, negative, or zero.

num=int(input("enter number:- "))

if num % 2==0:
    print("positive num!!")
    if num==0:
        print("zero found")
else:
    print("negative num!!")

    #it's done