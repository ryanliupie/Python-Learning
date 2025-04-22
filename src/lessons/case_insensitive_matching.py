import re 

cars = re.compile(r"mclaren", re.I) # pattern simply finds "mclaren" without caring if there are uppercase or lowercase values

print(cars.search('A mcLAReN is a hard car to drive.').group()) #.search looks for the text, and .group() pulls it out when matched 
