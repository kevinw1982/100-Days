print("Welcome to Python Pizza Delivery")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

final_bill = 0
if size == "S":
    final_bill += 15
elif size == "M":
    final_bill = 20
elif size == "L":
    final_bill = 25
else:
    ("You have entered wrong inputs")

if pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill += 3

if extra_cheese == "Y":
    final_bill += 1

print(f"The total for your pizza is £{final_bill}.")