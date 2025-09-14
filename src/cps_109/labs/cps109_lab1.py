# CPS 109 Lab 1 
# Questions 1 through 5 
# Creator: Ryan Liu
# Professor: Lugez

import math

# Question 1.  

celsius = float(input("Enter a temperature in Celsius: ")) 
fahrenheit = celsius * (9 / 5) + 32
kelvin = celsius + 273.15 

print("The temperature in Fahrenheit:", round(fahrenheit, 2))
print("The temperature in Kelvin:", round(kelvin, 2))

# Question 2.

coefficient_a = float(input("Enter the value of the polynomial coefficient 'a': "))
coefficient_b = float(input("Enter the value of the polynomial coefficient 'b': "))
coefficient_c = float(input("Enter the value of the polynomial coefficient 'c': "))

discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c

if discriminant > 0: 
    x1 = (-coefficient_b + math.sqrt (discriminant)) / (2 * coefficient_a)  
    x2 = (-coefficient_b - math.sqrt (discriminant)) / (2 * coefficient_a)
    print("There are two roots:", round(x1, 2),"and", round(x2, 2)) 

elif discriminant == 0: 
    x = -coefficient_b / (2 * coefficient_a)
    print("There is one root:", round(x, 2)) 

else:
    print("There are no real roots.")

# Question 3. 

side_a = float(input("Enter the length of the triangle for side 'a': "))
side_b = float(input("Enter the length of the triangle for side 'b': "))
side_c = float(input("Enter the length of the triangle for side 'c': "))

maximum_value = max(side_a, side_b, side_c)
result = side_a + side_b + side_c - max(side_a, side_b, side_c)

print(result > maximum_value)

# Question 4. 

a = float(input("Enter the side length (a) of a regular pentagon: "))
area = 1 / 4 * (math.sqrt(5 * (5 + 2 * (math.sqrt(5))))) * (a ** 2) 

print("The area of the pentagon:", round(area, 2))

# Question 5. 

n = int(input("Enter an integer value: "))
golden_ratio = (math.sqrt(5) + 1) /2 
function = ((2 + golden_ratio) / (5) * (golden_ratio ** n)) + ((3 - golden_ratio) / (5) * (golden_ratio ** - n))

print("The nth Fibonacci number:", round(function, 2))





