# A local variable is a variable that is defined inside a function and cannot be accessed outside of it

def number():
    y = 90

number()
#print(y) # in this case, y is inside the function (local variable) so when we try to print "y" outside the function, it would result in an error

def number():
    y = 90
    print(f"the number is {y}")

number() #now when we call the function y would get printed because "y" is delcared inside the variable allowing the print statement to access it

#--------------------------------------------------------------------------------------------------------

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(eggs)

spam() # in this case, it is important to note local scopes cannot use variables in other local scopes, so even if names match "eggs" they are independent to their own local scope. This also prints 0 first then 99 due to the call stack we learnt earlier


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------


# A global variables is a variable that is defined outside any function and is accesible throughout an entire python program even inside functions

y = 20 

def number():
    print(y) # Y would still get printed even though we are accessing it inside the function of "number"

number()
print(y) # Y is also accessible outside the function 


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------


# Even though we can use the same variables, it is best to avoid this 

def spam():
    eggs = 'local spam'
    print(eggs)

def bacon():
    eggs = 'local bacon'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)

# these are three different variables but it looks confusing right? So it best to use different variables. 


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------


# We can also modify the global variable to to another value 


def spam():
    global eggs 
    eggs = 'spam'

eggs = 'bacon'
spam()
print(eggs)

# in this "global eggs" just refers to "we are going to change this eggs variable" 
# so the code reads --> eggs is "bacon" right now. Then lets call the function spam()
# ok so we want to change the initial global variable from 'bacon' to 'spam'
# then we will print out the new eggs variable which is 'spam'

#--------------------------------------------------------------------------------------------------------

def spam():
    global eggs 
    eggs = 'spam'

def bacon():
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42 
spam()
print(eggs)

# the global variable eggs is 42 right now 
# lets call the spam() function 
# oh we want to change eggs into 'spam'
# print(eggs) and we get 'spam'