# remember that python uses 0 based indexing.
# string slicing is like "start at index x, then stop right before y" 

# [start : end : step]

card_number = "1234-5678-9017" 

print(card_number[0:4]) # start at index 0 but stop before 4
print(card_number[4]) # index "-" --> 0 = 1, 1 = 2, 2 = 3, 3 = 4, 4 = - 
print(card_number[5:9]) # start at index 4, and print only the middle values 
print(card_number[-1]) # prints last number of the index, the lower -2, -3, the more it goes towards the beginning

print(card_number[::2]) # prints every second character (step)
print(card_number[::3]) # prints every third character (step)

last_4 = card_number[-4:] # prints last 4 digits of the string
print(last_4)

reverse = card_number[::-1] # this reverses the entire string
print(reverse)