import random 

# ask a user to roll the dice 
# program outputs value and the display of the face of the dice 

print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") #uni-code characters 
# ● ┌ ─ ┐ │ └ ┘


"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘", 
    ), 

    2: ("┌─────────┐", 
        "│      ●  │", 
        "│         │", 
        "│  ●      │", 
        "└─────────┘", 
    ), 

    3: ("┌─────────┐", 
        "│      ●  │", 
        "│    ●    │", 
        "│  ●      │", 
        "└─────────┘", 
    ),

    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘", 
    ),

    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘", 
    ),

    6: ("┌─────────┐", 
        "│ ●  ●  ● │", 
        "│         │", 
        "│ ●  ●  ● │", 
        "└─────────┘", 
    )

}        

dice = []
total = 0 

num_of_roll = int(input("How many dice do you want to randomly roll? (1 - 6): "))

for die in range (num_of_roll):
    dice.append(random.randint(1, 6))

for line in range(5): 
    for die in dice: 
        print(dice_art.get(die)[line], end="")
    print()


for die in dice: 
    total += die
print(f" total: {total}")





