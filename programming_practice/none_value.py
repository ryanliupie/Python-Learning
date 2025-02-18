# None is the equivalent to "null" in other programming language such as C, it represents the absense of a value. 

a = None 
b = None 
print( a is b)
# in this context, there is only one None object in python so even if you assign 100 variables with the value of None, it points to same None.

#----------------------------------------------------------------------------------------

print(bool(None)) # bool converts value to True or False
print(None == False)
print(None == 0)
print(None == "")
# in this context, None is its own object, meaning it is not equal to False, 0 or "" (empty string). None == False is False because None is its own object, cannot be True.

#----------------------------------------------------------------------------------------

def example():
    pass

print(example())
# when you call this function, it returns nothing because there is no return statement
# this is usally used as a placeholder for something later on

#----------------------------------------------------------------------------------------

