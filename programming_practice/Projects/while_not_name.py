name = "" 

while not name: 
    print("Enter your name: ")
    name = input()

# the name starts as an empty string and "while not name" says "while this name is empty we are going to keep looping"
# tf we enter a name it will stop 

print("How many guests will you have?: ")
numOfguests = int(input())
if numOfguests:
    print("Be sure to have enough room for all your guests!")
print("Done")
    
# this asks us how many guests we have where we can input the number of how many comes 
# if we input a number, it will display that we to be sure we have enough room 
