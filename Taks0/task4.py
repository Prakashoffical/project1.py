# Write a program to input a character and check whether it is a vowel (a, e, i, o, u) or a consonant.

# vowel = ("a,e,i,o,u")
# char = (input("enter your charectr : ")).lower()
# if len(char) == 1:
#         print("vowel")
# else:
#         print("consonst")

# it's work

user=input("enter charectr: ")

if user.lower() in "aeiou":
        print("it is vowel")
else:
        print("it's consonst")