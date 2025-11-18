# Creator: Ryan Liu 
# Student ID: 501195710 
# Course: CPS-109 

# Problem Statement: 
'''
A start-up in San Francisco called "Turtle's Lab" is starting to hire employees, and to save time, they randomly generate employee IDs and store them in a file called "rough_ids.txt" 
Some of the employee ID's are valid, while some of them are not. Turtle's lab's parameters around these ID's which include the following:  

- Must be 6 digits long 
- The initial digit cannot be 0 
- There cannot be any whitespaces
- The sum of the digits must be greater than 10 

After identifying the digits, classify each digit as either a Junior employee, Mid-level employee or Senior Level employee based on the initial digit: 
- 1-3: Junior 
- 4-6 Mid-Level
- 7-9 Senior

Once classified, store these employee ID's attached with its position level in a new file called "finalized_ids.txt"

'''
with open("rough_ids.txt", "r") as f: 
    for line in f: 
        print(line)


