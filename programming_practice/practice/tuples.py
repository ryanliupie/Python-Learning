# Tuple = immutable ordered collection of data 

student = ("Ryan", 45, "male")

print(student.count("male"))
print(student.index("Ryan"))

# tuples have limited methods since they are immutable. 
# you cannot use .append(), .remove() etc... 