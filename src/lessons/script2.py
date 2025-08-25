from lessons.script1 import * 
dog3 = Animals("Aiko", 5)
print(dog3.name, end = ": ")
print(dog3.age)

# so now if we run this, this runs as the main script, but only gives us the dog3 value
# because the "__name__ == __main__" in script 1 is saying that that script will only 
# execute only if executed directly. Since we are executing script2, script1 is not 
# being executed directly, so it will not give us dog1 and dog2. 

# This is useful for testing scripts