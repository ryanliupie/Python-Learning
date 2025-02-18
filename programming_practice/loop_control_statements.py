# Loop control statements = change a loops execution from its normal sequence 

# break =     This is used to terminate the loop entirely 
# continue =  This skips to the next interation of the loop 
# pass =      does nothing, acts as a placeholder 

while True:
    name = input("Enter your name: ")
    if name != "":
        break

# so for this, while True expresses that this statement is true and it asks us to input our name
# if the name is not an empty string, we will break, so this means if we enter a name it will break
# if we do not enter a string, it will continue looping

phone_number = "416-876-2317"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# for every character in the variable phone number, if the character is equal to "-"
# we will continue and skip over them
# then we we print out the values in the variable without "-"

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
    
# for every value in the range between 1 and 21
# we will pass or skip over 13 and print the rest of the range



