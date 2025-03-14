# Dictionary = A mutable key-value pair that cannot contain duplicates 

cars = {"Japanese": "Toyota",
        "European": "Audi",
        "American": "Tesla",
        "Italian": "Ferrari"}

# print(dir(cars))     # this lets you see all the methods used in a dictionary
# print(help(cars))    # this lets you see what each method can do

# print(cars.get("Japanese")) # this lets you get the value of the pair 
# print(cars.get("Germany")) # this would display none

# cars.update({"Italian": "Pagani"})
# cars.pop("American") 
# cars.popitem() # pops last key value pair
# ------------------------------------------------------
for key in cars.keys(): # prints all keys 
    print(key)

# ------------------------------------------------------
for value in cars.values(): # prints all values 
    print(value)
# ------------------------------------------------------


