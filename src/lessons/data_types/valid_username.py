# validate user input exercise 
# 1. username is not more than 12 characters
# 2. username must not contain spaces 
# 3. username must not contain digits 

username = input("Enter a username: ")

if len(username) > 12:
    print("That username is too long, please try again")
    
elif not username.find(" ") == -1: # if the username does equal to -1, then there is a problem since a string with not spaces returns a -1. If it does not equal it and returns 1,2,4,6 etc... there is a space 
    print("You cannot have any spaces, please try again.")

elif not username.isalpha():
    print("You cannot have any digits, please try again.")

else: 
    print(f"[{username}] is a cool name dude!")




       
