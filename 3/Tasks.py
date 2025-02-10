print("Welcome to the rollercoaster")
height = int(input("What is your height in cm's "))
bill = 0
if height >= 120:
    print("You can ride the Rollercoaster")
    age = int(input("Please enter your age "))
    if age <= 12:
        bill = 5
        print("Child tickets are £5")
    elif age <=18:
        bill = 7
        print("Youth tickets are £7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everthing is ok have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are £12")

    wants_photo = input("Do you want a photo taken? type y or n ")
    if wants_photo == "y":
        bill += 3
    print(f"Your total price is £{bill}")
else:
    print("Sorry you have to grow taller before you can ride")

print(10 % 3)

number = int(input("What is the number you want to check: "))
if number % 2 == 0:
    print("your number is even!")
else:
    print("Your number is odd!")