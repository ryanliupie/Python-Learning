# Exception Handling
# getting an error in python is not good for real world programs because they would crash entirely 
# instead, you want the program to detect errors, handle them, and then continue to run

#numerator = int(input('Enter a number to divide: '))
#denominator = int(input('Enter a number to divide by: '))
#result = numerator / denominator 
#print(result)

# if we enter a number that is a decimal, string, or some equation that makes no sense it would result in ERROR, ERROR, ERROR, ERROR, ERROR

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# Now in this, we are going to "try" if the code works and if it doesn't specify to the user "something went wrong"
# surround the code that will be executable with "try" where the code would work if everything went well

try:
    numerator = int(input('Enter a number to divide: ')) # considered dangerous code as we do not know what the use might put
    denominator = int(input('Enter a number to divide by: ')) # considered dangerous code as we do not know what the use might put
    result = numerator / denominator 
    print(result)

except Exception:
    print('something went wrong') # this works but not best practice as the program does not specify what type of exception it is to handle all exceptions

#--------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    numerator = int(input('Enter a number to divide: ')) 
    denominator = int(input('Enter a number to divide by: ')) 
    result = numerator / denominator 
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero man") # we specifically handle errors when one tries to divide by 0
except ValueError:
    print("You have to type in a number") # we specifically handle errors when a person types in a non numerical value
except Exception:
    print('something went wrong')

#--------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    numerator = int(input('Enter a number to divide: ')) 
    denominator = int(input('Enter a number to divide by: ')) 
    result = numerator / denominator 
    print(result)
except ZeroDivisionError as e: # this would print out the actual exeception that occured rather than only the print statement associated
    print(e)
    print("You can't divide by zero man") 
except ValueError as e:
    print(e)
    print("You have to type in a number")
except Exception as e:
    print(e)
    print('something went wrong')


#--------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    numerator = int(input('Enter a number to divide: ')) 
    denominator = int(input('Enter a number to divide by: ')) 
    result = numerator / denominator 
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero man") 
except ValueError as e:
    print(e)
    print("You have to type in a number")
except Exception as e:
    print(e)
    print('something went wrong')
else:
    print(result) # we can add an else block if the person enters 2 valid values 
finally:
    print("Think a bit further") # this clause will always execute 
    # for instance you enter "8 / 0". It will print out "You can't divide by zero man" and "Think a bit further"  
    # Or even if you do "2/2". It will print out the value of "1" and "think a bit further" which does not make sense. This is why it is mainly used for file handling