
import random

def getAnswer (answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook no so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
r = random.randint(1,9) # this generates a random variable from 1 to 9 and assigns it the variable r
fortune = getAnswer(r) # this calls the function ans the answerNumber is the parameter where r is the argument we pas through
print(fortune) # if we want to see the function we called, we can use a print statement 



