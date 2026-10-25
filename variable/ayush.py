# Accept input from the user
bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage: "))
num_people = int(input("Enter the number of people: "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total bill
total_bill = bill_amount + tip_amount

# Calculate each person's share
per_person = total_bill / num_people

# Format the values to 2 decimal places and display
tip_amount = f"Rs. {tip_amount:.2f}"
total_bill = f"Rs. {total_bill:.2f}"
per_person = f"Rs. {per_person:.2f}"

# Display the wicked results
print(f"Tip Amount : {tip_amount}")
print(f"Total Bill : {total_bill}")
print(f"Per Person : {per_person}")
