#Calculator 

print("1 = add")
print("2 = subtract")
print("3 = multiply")
print("4 = divide")

option = int(input("Choose an operation: "))

if(option in [1,2,3,4]): #this is the list and because of "int" we have to add an integer 1,2,3, or 4 
    num1 = float(input("Enter first number: ")) #enter first number (can be decimal, negative, or whole because of the float data type)
    num2 = float(input("Enter second number: ")) #enter second number (can be decimal, negative, or whole because of the float data type) 

    if (option == 1):
        result = num1 + num2
        print(result)

    elif (option == 2): 
        result = num1 - num2
        print(result)
    
    elif (option == 3):
        result = num1 * num2
        print(result)

    elif (option == 4):
        result = num1 / num2
        print(result)
        
else:
    print("Incorrect option selected, please try again")

print(f"The result of the operation is: {result}")