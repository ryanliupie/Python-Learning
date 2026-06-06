'''
zip() = This function combines multiple iterables (lists, tuples, sets, dict)

# Note an "iterable" is any object that can provide its elements at a time which means you can loop through it with a for loop 

zip() returns a tuple object(iterator) such as <zip object at 0x000002F6CAC1BD80> if we were to print it

If we wanted to see the data, we could type cast it into a list for example: 

- [('Ryan', 35), ('Arthur', 34), ('Lucid', 33)]

'''

names = ["Ryan", "Arthur", "Lucid"]
ages = [35, 34, 33]
jobs = ["Pilot", "Mechanic", "Helpdesk"]

data = (zip(names, ages, jobs))

for name, age, job in data: 
    print(f"{name}: {age}: {job}")