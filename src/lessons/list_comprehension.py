'''
List comprehension = A concise way to create lists in python
[expression for value in iterable if condition] 

Just reverse the thinking. Do the regular loop logic first and then write output code last in the first spot 
'''




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

# -----------------

nums = [300, 400, 500]
print([num for num in nums if num >= 400])

# -----------------

nums2 = [1, 2, 3, 4, 5, 6]

print([num for num in nums2 if num % 2==0])

# -----------------

logs = [
    {"ip": "10.0.0.1", "status": 200},
    {"ip": "10.0.0.2", "status": 500},
    {"ip": "10.0.0.3", "status": 403},
]

ips = [log["ip"] for log in logs if log["status"] >= 400]
print(ips)

# -----------------

counts = {"10.0.0.1": 2, "10.0.0.2": 5,"10.0.0.3": 1,}

ips2 = [ip for ip, count in counts.items() if count >=3]
print(ips2)

# -----------------

logs2 = [
    {"ip": "10.0.0.1", "bytes": 1200},
    {"ip": "10.0.0.2", "bytes": 5000},
    {"ip": "10.0.0.1", "bytes": 3000},
    {"ip": "10.0.0.2", "bytes": 6000},
]

ips3 = list({log["ip"] for log in logs2 if log["bytes"] > 4000})
print(ips3)
