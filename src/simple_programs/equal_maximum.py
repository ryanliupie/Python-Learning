# equal and maximum 
# no max function

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 == num2 == num3: 
    print("All three numbers are equal values")

elif num1 == num2: 
    print("The first two numbers are equal")

elif num2 == num3: 
    print("The second and third numbers are equal")

elif num1 == num3: 
    print("The first and third numbers are equal")

elif num1 > num2 and num1 > num3: 
    print("The first number is the maximum")

elif num2 > num1 and num2 > num3: 
    print("The second number is the maximum")

else: 
    print("The third number is the largest")

