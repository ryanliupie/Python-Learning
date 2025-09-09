# CPS 109 Lab 1 
# Questions 1 - 5 
# Creator: Ryan 
# ---------------

import math

# Question 1.  

c = float(input("Enter a temperature in Celsius: ")) # i used the "float" type since the temperature could contain decimal values 

f = c * (9/5) + 32
k = c + 273.15 

print("The temperature in Fahrenheit is", f)
print("The temperature in Kelvin is", k )


# Question 2. 

a = float(input("Enter the value of the polynomial coefficient of 'a': "))
b = float(input("Enter the value of the polynomial coefficient of 'b': "))
c = float(input("Enter the value of the polynomial coefficient of 'c': "))



x2 = -b - (math.sqrt(b ** 2) - (4 * a * c) / 2 * a)


print(x2)