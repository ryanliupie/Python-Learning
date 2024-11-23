# bmi calculator 

name1 = "ryan"
height_m1 = 6
weight_kg1 = 95

name2 = "jaideep"
height_m2 = 6 
weight_kg2 = 85 

name3 = "steven"
height_m3 = 6 
weight_kg3 = 75 

def bmi_calculator(name, height_m, weight_kg): ## 3 parameters 
    bmi = weight_kg / (height_m ** 2)
    print(f" The bmi is: {bmi}")
    if bmi < 25: 
        return name +  " is not overweight" # one space at beginning to space out text when printed
    else:
        return name + " is not overweight" # one space at beginning to space out text when printed
    
result1 = bmi_calculator(name1, height_m1, weight_kg1 ) # We call the function with these variables we initialized
result2 = bmi_calculator(name2, height_m2, weight_kg2 ) # We call the function with these variables we initialized
result3 = bmi_calculator(name3, height_m3, weight_kg3 ) # We call the function with these variables we initialized

print(f"The outcome is: {result1}")
print(f" The outcome is: {result2}")
print(f"The outcome is: {result3}")