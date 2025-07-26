# List comprehension = A concise way to create lists in python
#                       [expression for value in iterable if condition] 


test = [print(x) for x in range(1, 11)]

# -----------------

triples = [y * 3 for y in range(2, 21)]
print(triples)

# -----------------

fruits = ["apple", "mango", "watermelon", "papaya"]
uppercase = [fruit.upper() for fruit in fruits]
print(uppercase)

# -----------------

numbers = [1, -2, 3, -8, -6, 4]
positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)

# -----------------

numbers = [1, -2, 3, -8, -6, 4]
negative_numbers = [num for num in numbers if num <= 0]
print(negative_numbers)

# -----------------

numbers = [1, -2, 3, -8, -6, 4]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


