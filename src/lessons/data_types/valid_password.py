# Creator: Ryan Liu 
# 04/22/2025

# Validate a Password Input
# 1. The password must be at least 8 characters long
# 2. The password must contain atleast one digit
# 4. The password must contain atleast one uppercase letter
# 5. The password must be NOT contain any spaces 

password = input('Enter a password: ')

if len(password) < 8:
    print("The password is too short, please try again.")

elif password.isalpha():
    print("You must include a digit, please try again.")

elif not any(char.isupper() for char in password): # "if the condition is false". The "any()" function returns true if atleast one item in the iterable is True. Then, for every character in password, it runs the "char.isupper" method to see if a value is in uppercase 
    print("Please include atleast one uppercase value, please try again.")

elif not password.find(" ") == -1: # if the password does not equal to -1, then...
    print("You cannot have any spaces, please try again.")

else:
    print(f"[{password}] is secure!")