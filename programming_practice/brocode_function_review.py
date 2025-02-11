# Remember a function is a collection of code to perform a specific action 

def happy_birthday(name, age): #the function is happy_birthday and the parameters are name and age. It could be x or y too because they are just placeholders when we want to call the function
    print(f"Happy birthday to {name}")
    print(f"you are {age} years old")
    print(f"Happy birthday to {name}")

happy_birthday("Ryan", 20) #This is where we call the function and display what we made inside the function. 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}") #.2f is rounding the amount to 2 decimal places

display_invoice("Ryan", 300.4567, "Jan 1, 2025") #These are the arguments we pass through when calling the function based on the parameters we specified

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_numbers(a,b):
    return a + b #by using return, you can call the function many times with different inputs and you can use this for other calculations

#result = add_numbers(5,6)
#result2 = add_numbers(7,8)
#print(result1)
#print(result2)
print(add_numbers(5,6))
print(add_numbers(7,8))

#instead of 

number1= 2 
number2 = 3
x = number1 + number2
print(x)

number3= 4 
number4 = 5
x = number3 + number4
print(x)
