# ROCK, PAPER, SCISSORS GAME 

import random
import sys

wins = 0 
losses = 0 
ties = 0 

# Main Game Loop 
while True: 
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    while True:
        playerMove = str(input('Enter (r) for Rock, Enter (p) for Paper, Enter (s) for Scissors, or Enter (q) for Quit: '))
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Invalid Input: Type one of r, p, s, or q.')

# Displays the Players Choice  
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

# Displays Computers Choice 
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2: 
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

# Displays Wins/Losses/Ties 
    if playerMove == computerMove:
        print('It is a tie')
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You lose!")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1