name = str(input("Enter a name: "))
phone_number = input("Enter your phone number: ")

result = len(name)
result = name.find("r") # finds first occurence 
result = name.rfind("e") # find last occurence
result = name.capitalize() # capitalizes first letter of your name
result = name.upper() # makes letters all uppercase
result = name.lower() # makes all letters lowercase
result = name.isdigit() # returns true only if string contains digits 
result = name.isalpha() # returns true of string is one word. Returns false if string contains numbers and has multiple strings as "spaces" are not alphabetical characters 
print(result)

result2 = phone_number.count("-") # counts how many times the specified value occurs
result2 = phone_number.replace("-", ".") # replaces value with something else you want

print(result2)

# ----------------------------------------------------------------------


