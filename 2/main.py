#Day 2 final project
print("Welcome to the tip calcuator!")
bill = float(input("What was the total bill? £"))
tip = float(input("How much tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = round((bill + total_tip_amount) / people, 2)
print(f"Each person should pay: £{total_bill}")