# ATM machine in python
print("welcome to ATM machine ")
      
Balance=1000.0
pin_code=1111

print("processing........")

user=int(input("enter your pin_code : "))

if user == pin_code:
    while True:
        print(''' 
               ============================  ATM MENU ==========================
               1.Balance check
               2.withdraw Balance
               3.Deposite Balance
               4.exit

              ''')
        choice = input("Enter you'r valid choice [1-4] : ")
        if choice == '1':
            print(f"your currentl Balance ls Rs. {Balance}")
        elif choice == '2':
            withdraw_amt=float(input("withdeaw Amount : Rs. "))
            withdraw_amt >= Balance 

            print(f"your avable amount Rs {Balance}")

            Balance -= withdraw_amt or Balance <= withdraw_amt

            print(f"Rs.{withdraw_amt} withdraw successfully , remainin balance is Rs. {Balance}")
         
            
        elif choice == '3':
            deposite_amt=float(input("Enter ypur Deposite amt : Rs. "))
            Balance += deposite_amt
            print(f"Rs .{deposite_amt} Deposited successfully .New balance is Rs: {Balance}")
        elif choice == '4':
            print("Thank you for using our service💳")

            break


else:
    print("⛔ incorrect pin_code , please try again ")