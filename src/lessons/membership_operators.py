# Membership operators: these are used to test whether a value is found in a sequence
#                       (string, list, tuple, dictionary, or set)

#                       1. in 
#                       2. not it

grades = {"Ryan": "A+",
         "Patrick": "B-", 
         "Bob": "D+"}

student = input("Enter a students name in your class: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}.")

else:
    print(f"{student} is no where to be found.")

