# Write a program where if the total shopping bill is greater than 1000, apply a 10% discount and print the final amount

bill=1100 #input("enter bill amount :")

if bill>=1000:
    discount=bill*10/100
    total_bill=discount-bill


    print("congratulations you got 10% discount")
    print(f"discount : {discount}")
    print(f"total bill after discount : {total_bill}")
    

else:
    print(f"your bill ls {bill}")

    #it's done