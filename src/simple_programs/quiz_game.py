# Quiz game 

questions = (
    "What car is Japanese?", 
    "Which animal lays the largest eggs?: ", 
    "Which planet is no longer a planet?: ", 
    "What certification needs atleast 5 years of experience?: ", 
    "How many bones are in the human body?: " 
    )


options = (
    ("A. GMC", "B. Dodge", "C. Nissan", "D. Tesla"), 
    ("A. Chicken", "B. Crocodile", "C. Duck", "D. Ostrich"), 
    ("A. Saturn", "B. Jupiter", "C. Venus", "D. Pluto"), 
    ("A. Security+", "B. CISSP", "C. AWS-SAA", "D. Network+"), 
    ("A. 320", "B. 206", "C. 197", "D. 203")
) 

answers = ("C", "D", "D", "D", "B")
guesses = []
score = 0 
question_num = 0

for question in questions:
    print("----------")
    print(question)
    for option in options[question_num]: # for every option in the options given, give us the index of 0 which is the "cars" option which not good, we need to interate each one, look below!! 
        print(option)

    guess = input("Choose an answer either (A, B, C, D): ").upper() # the .upper makes sure that if user types in a lowercase, the program would take it as a uppercase 
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 
        print("Correct!")

    else:
        print("Incorrect!")
        print(f"The correct answer is '{answers[question_num]}'.")
    question_num += 1 # now this interates with all the options. 0 = cars, 1= eggs, 2 = planets, 3 = certs, 4 = bones 


print("--------------")
print("    Result    ")
print("--------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
    
score = int(score / len(questions) * 100) #gets the score by seeing all the questions you got right and dividing it by how many questions there are 
print(f"Your score is: {score}%")
