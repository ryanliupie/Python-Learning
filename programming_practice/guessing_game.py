import random # this module allows functions to generate random numbers 

def guess (x): # we create a function called 'guess' and it we'll call an input called 'x'. This 'x' is a parameter which the function needs in order for the function to work.
    random_number = random.randint(1, x) #random.randint generates a random integer between a and b. a<= N <=b
    guess = 0 # this makes sure that guess has an initali value before you can start comparing to random_number that the computer generates. Python would not know what to compare random_number to  
    while guess != random_number: #a while loop will continue to interate util a certain condition is met. So when we look at this, we have to take in account the "while". So each time i guess incorrect, the loop will keep going, allowing me to try again AS LONG AS THE GUESS IS NOT THE RANDOM NUMBER BECAUSE THEN IT WILL STOP. You can look at this like "while our guess is not the same as the random number you are hiding, I am going to keep guessing"
        guess = int(input(f' Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low, try again')
        elif guess > random_number:
            print('Too high, try again')

    print(f" Good job, you got the correct number right which was {random_number}") #Once the random number is picked, we can simply print it out.



guess(10) # This number 10 represents x. So in this case, we are referring to `1 and 10` where the user would have to pick a number from. 