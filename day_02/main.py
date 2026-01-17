print("Welcome to the tip calculator")

bill_amount = float(input("What is the total bill amount?\n"))
tip_percentage = int(input("What tip percentage would you like to give? 10%, 12% or 15%\n"))
number_of_people = int(input("How many people will split the bill?\n"))

tip_rate = tip_percentage / 100
total_tip = tip_rate * bill_amount
total_bill_with_tip = bill_amount + total_tip
bill_per_person = total_bill_with_tip / number_of_people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: {final_amount}")
