number: bool = True 

if type(number) is int: 
    print(f"'{number}' is not an integer")

else: 
    if type(number) is bool: 
        print(f"'{number}' is a boolean expression")

number2: int = 4 

list = [1, 2, 3, 4, 5]

if len(list) >= 4: 
    print("the list is long")

else:
    print("Hell yeah")