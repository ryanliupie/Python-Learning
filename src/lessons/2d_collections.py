# a 2d list is a list that holds other lists, so each element is itself a list in the 2d list 
#  it is commonly used for representing matricies, grids, or spreadsheets 

fruits = ["apple", "pear", "banana", "coconut"] # 1d list 
vegetables = ["lettuce", "peas", "potatoes"] # 1d list 
meats = ["chicken", "beef", "fish"] # 1d list 

groceries = [fruits, vegetables, meats] # 2d list 

print(groceries[0]) # fruits list 
print(groceries[1]) # vegetables list 
print(groceries[2]) # meats list  

print(groceries[0][0]) # "row 0: column 0" like coordinates where we look at the "fruits list" and get "apple"
print(groceries[2][2]) # gets us "fish"
print(groceries[1][2]) # gets us "potatoes"


# you could also write it like this: 

groceries2 = [
    ["apple", "pear", "banana", "coconut"],  
    ["lettuce", "peas", "potatoes"],  
    ["chicken", "beef", "fish"] 
]

for collection in groceries2: # "for the collection in the groceries2"
    for food in collection: # "for every food in that collection"
        print(food, end=" ") # "print out every food on each line with a space" 
    print() # creates newline after each collection gets iterated over

# remember that any name after "for" is a temporary variable. 
# so it is like for each "x" in this actual collection "y", do something with "x"

# ---------------------------------------------------------------------------------------------------------------------------------

# 2d tuples are the same thing, a tuple that holds other tuples:  

phone_number = (
    (2, 4, 7), 
    (3, 1, 5), 
    (7, 6, 9, 2)
)

for numbers in phone_number:
    for num in numbers: 
        print(num, end="")
    print()
