'''Write a Python program that validates a user's password against the five rules below. Clearly indicate which
specific requirements were NOT met.
Requirements:
◆ At least 8 characters long
◆ Contains at least one uppercase letter (A-Z)
◆ Contains at least one lowercase letter (a-z)
◆ Contains at least one digit (0-9)
◆ Contains at least one special character (! @ # $ % ^ & * etc.)'''

password="Sujan710@"

is_upper=False
is_lower=False
is_digit=False
ls_special=False

if len(password)<8:
    print("password must have 8 character")

for i in password:
    if i.isupper():
        is_upper=True
    elif i.islower():
        ls_lower=True
        
    elif i.isdigit():
        is_digit=True
    elif i in "!@#$%^&*(?)":
        is_special=True

if not is_upper:
    print("password must need one upper characeter")

if not is_lower:
    print("password must be one lower characeter")
if not is_digit:
    print("password must be at least one digit")


