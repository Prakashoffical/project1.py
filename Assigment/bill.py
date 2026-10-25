'''
Accept the bill amount, tip percentage and number of people from the user.
• Convert the inputs to the correct data types. 
• Calculate and display the tip amount, the total bill and each person's share. 
• Format every monetary value to 2 decimal places using f-strings. 
SAMPLE OUTPUT 
Bill = 2000, Tip = 10%, People = 4 
Tip amount : Rs. 200.00 # need to convet on persantage
Total Bill : Rs. 2200.00 
Per Person : Rs. 550.00
'''
#input from user
bill =float(input("enter total bill rs:- "))
tips_persantage =float(input("tip rs:- ""%"))
total_person =input("number person:- ")



# persantage from bill amount
tip_amount=((bill*tips_persantage)/100)
print("tip amount:-",tip_amount,)


# tips_persantage 
tip_persantage=(tip_amount / bill) * 100
print("tips:- ",tip_persantage,"%")

#total bill  and tips amount
total_bill=(bill+tip_amount)
print("total bill rs:- ",total_bill)

#each person's share
# per_person=(f"{total_bill} / {total_person}")                          # NEED TO FIXED HERE
per_person= int(total_bill / total_person)                     
print("per_person rs:- ",per_person)


a=f"(bill:{bill}, tip:{tip_persantage}%, people:{total_person})"
print(a)






