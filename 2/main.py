#Day 2 final project
print("Welcome to the tip calcuator!")#
bill = int(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))
total = bill + tip / people
print("Each person should pay: ")