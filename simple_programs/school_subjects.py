# School Subjects 
# Creator: Ryan Liu

def university_classes (favourite_subject):
    print(f'my favourite subject is {favourite_subject}')
    unliked_subject = input('What is your least favourite subject? (math, science, english, or chemistry): ')
    if unliked_subject == 'math' or 'science' or 'chemistry': # this would be incorrect because 'science' and 'chemistry' are not conditions since they are not being compared. Because python see's them as strings, they are always evaluated to True
        print('I am the opposite, I love those classes') # this line would always be evaluated because above it is saying 'if (unliked_subject == "math") or True or True'. Since atleast one True is found in a 'or' operator it would evaluate to True
    elif unliked_subject == 'english':
        print('Same, I do not like writing')
    else:
         print('Please enter a subject: ')

university_classes("chemistry")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def university_classes (favourite_subject):
    print(f'my favourite subject is {favourite_subject}')
    unliked_subject = input('What is your least favourite subject? (math, science, english, or chemistry): ')
    if unliked_subject == 'math' or unliked_subject == 'science' or unliked_subject == 'chemistry': # now these are all conditions that python can see since we are comparing them now to evaluate to True or False
        print('I am the opposite, I love those classes') 
    elif unliked_subject == 'english':
        print('Same, I do not like writing')
    else:
       print('Please enter a subject: ') # this works, however, in order for the person to enter a subject again if they misspelled, they would need to run a program, so we need to incorporate something that will loop until a condition is met

university_classes("chemistry")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def university_classes (favourite_subject):
    print(f'my favourite subject is {favourite_subject}')
    unliked_subject = '' # we initialize this variable so that python can see it when it begins the while loop 
    while unliked_subject != 'math' or unliked_subject != 'science' or unliked_subject != 'english' or unliked_subject != 'chemistry': # this does not make sense because while unliked subjects is not equal to x, the loop will keep happening since we are also using the 'or' operator. For example, if we enter math. math != math is false because it is. math != science is True. And remember that if one of the "OR" conditions is True, the whole thing evaluates to True even though we entered 'Math' meaning the loop will keep happening even though we wanted it to stop by entering 'math'. If I enter a random input 'fi2394f', it would work because none of those values match. However, it is more likely someone would enter a subject since we prompt them to do to which is the main issue. 
        print('Please enter a subject: ')
    unliked_subject = input('What is your least favourite subject? (math, science, english, or chemistry): ')
    if unliked_subject == 'math' or unliked_subject == 'science' or unliked_subject == 'chemistry': 
        print('I am the opposite, I love those classes') 
    elif unliked_subject == 'english':
        print('Same, I do not like writing')
    else:
        print('Please enter a subject: ')

university_classes("chemistry")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def university_classes (favourite_subject):
    print(f'my favourite subject is {favourite_subject}')
    valid_subject = ['math', 'science', 'english', 'chemistry'] # this is a list that contains all the correct subjects that the user can enter. We enter this before so the python program knows what to use
    unliked_subject = '' # python needs to know what unliked_subject is before checking it in the while loop, if it is not initialized, the program won't know what to check
    while unliked_subject not in valid_subject: # this says "if unliked_subject is empty or invalid, please try again"
        print('Please enter a valid subject: ')
        unliked_subject = input('What is your least favourite subject? (math, science, english, or chemistry): ')
    if unliked_subject == 'math' or unliked_subject == 'science' or unliked_subject == 'chemistry': 
        print('I am the opposite, I love those classes') 
    elif unliked_subject == 'english':
        print('Same, I do not like writing')

university_classes("chemistry")