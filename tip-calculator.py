print("Welcome to the tip calculator!")
total_bill = float(input("What is your total bill? "))
tip_Percent = int(input("What percentage would you like to tip? "))
split_by = int(input("How many people to split the bill? "))

bill_plus_tip = (tip_Percent) / 100 * total_bill + total_bill

bill_per_person = bill_plus_tip / split_by

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay £{final_amount}")