'''Task 14.
Write a program to input marks and assign grades based on the following conditions:
• 90 and above → Grade A
• 80 and above → Grade B
• 70 and above → Grade C
• 60 and above → Grade D
• Below 60 → Fail
'''

marks=int(input("enter your marks:- "))

if marks >= 90:
    print("grade A")
elif marks >= 80:
    print("grade B")
elif marks >= 70:
    print("grade C")
elif marks >= 60:
    print("grade D")
else:
    print("fail")

    # it's done