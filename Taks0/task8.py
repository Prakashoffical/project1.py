# Write a program to check whether a string entered by the user is a palindrome (same forward and backward).
word=input("enter the value :" )
reversed_word=word[::-1]

if word == reversed_word:
    print("it's palindrome.")
else:
    print("it's not palindrome. ")


    #it's done