# Keyword arguments are a way to pass arguments to a function by explicitly naming each parameter and assigning it a value using "name=value" syntax

def greeting(name, age, city):
    print(f"my name is {name}, I am {age} years old, and I live in {city}.")


greeting(name="Bob", age = 23, city="New York")


for i in range (1,11):
    print(i, end=" ")

print("1", "2", "3", "4", sep="-")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_number = get_phone(country="Canada", area="ON", first="647", last="5423")

print(phone_number)

