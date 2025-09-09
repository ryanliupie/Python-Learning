# CPS 109 Lab 1 
# Questions 1 - 5 
# Creator: Ryan 
# ---------------

import math

# Question 1.  

c = float(input("Enter a temperature in Celsius: ")) # i used the "float" type since the temperature could contain decimal values 

f = c * (9/5) + 32
k = c + 273.15 

print("The temperature in Fahrenheight is", f)
print("The temperature in Kelvin is", k )


# Question 2. 

a = float(input("Enter the value of the poloynomical coffecient of 'a': "))
b = float(input("Enter the value of the poloynomical coffecient of 'b': "))
c = float(input("Enter the value of the poloynomical coffecient of 'c': "))



x2 = -b - (math.sqrt(b ** 2) - (4 * a * c) / 2 * a)


print(x2)