# Creator: Ryan Liu 
# 06/08/2025
# review 

import random 

low = 1 
high = 10 

while True: 
    number = random.randint(low, high)
    guess = int(input("Guess a number from 1 to 10: "))
    if guess == number: 
        print(f"Your guess of {guess} is correct!")
        break
    else:
        print(f"Your guess of {guess} is incorrect, it was {number}")
    