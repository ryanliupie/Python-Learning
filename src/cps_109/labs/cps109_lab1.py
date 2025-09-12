# CPS 109 Lab 1 
# Questions 1 - 5 
# Creator: Ryan 
# ---------------

import math

# Question 1.  

celsius = float(input("Enter a temperature in Celsius: ")) # i used the "float" type since the temperature could contain decimal values 

fahrenheit = celsius * (9/5) + 32
kelvin = celsius + 273.15 

print("The temperature in Fahrenheit:", fahrenheit)
print("The temperature in Kelvin is:", kelvin)


# Question 2. 

a = float(input("Enter the value of the polynomial coefficient of 'a': "))
b = float(input("Enter the value of the polynomial coefficient of 'b': "))
c = float(input("Enter the value of the polynomial coefficient of 'c': "))


x1 = -b + (math.sqrt (b ** 2) -  (4 * a * c)) / (2 * a)  
x2 = -b - (math.sqrt (b ** 2) -  (4 * a * c)) / (2 * a)  

print(x1) 
print(x2)

# Question 3. 

side_a = float(input("Enter the length of the triangle for side A: "))
side_b = float(input("Enter the length of the triangle for side B: "))
side_c = float(input("Enter the length of the triangle for side C:  "))

result = side_a + side_b + side_c - max(side_a, side_b, side_c)
print(result)

# Triangle inequality theorem 
# --> The sum of the lengths of 2 sides must be greater than the length of the third side



