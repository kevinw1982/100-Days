print('''
  ____________________________________________________________________
 *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a cross roads, where do you want to go? Type "Left" or "Right"').lower()

if choice1 == "left":
    choice2 = input('You have come to a lake. There is an island in the middle of the lake. '
          'Type "Wait" to wait for a boat. Type "Swim" to swim across the lake.').lower()
    if choice2 == "wait":
        choice3 = input('You arrived at the island unharmed '
                         'There is a house with 3 doors. One Red One Yellow and One Blue '
                         'Which do you choose?').lower()
        if choice3 == "red":
            print("You have entered a room with a large Lizzard and your eaten. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure Well Done!")
        elif choice3 == "Blue":
            print("There is a lion in this room. Game Over")
        else:
            print("you entered a different colour. Game Over")
    else:
        "You got attacked by Nessie. Game over"
else:
    print("You fell into a trap of snakes. Game over")
    



