# Keyword arguments are a way to pass arguments to a function by explicitly naming each parameter and assigning it a value using "name=value" syntax

def greeting(name, age, city):
    print(f"my name is {name}, I am {age} years old, and I live in {city}.")


greeting(name="Bob", age = 23, city="New York")


for i in range (1,11):
    print(i, end=" ")

print("1", "2", "3", "4", sep="-")


def phone_number(first, second, third):
    print(first + "-" + second + "-" + third)

phone_number(first="123", second="345", third="678")

