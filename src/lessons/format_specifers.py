# format specifiers = {value:flags} --> formats a value based on the given flag 

price1 = 234354.675
price2 = -64235.63465345534
price3 = 12355.99


# rounding to 2 decimal places 
print(f"Price 1 is ${price1:.2f}") 
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")


# prints out value 20 spaces to the right 
print(f"Price 1 is ${price1:20}") 
print(f"Price 2 is ${price2:20}")
print(f"Price 3 is ${price3:20}")


# insert 0 padding when printed 
print(f"Price 1 is ${price1:010}") 
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")


# left justify a value (pushes values to the left with 20 spaces on the right)
print(f"Price 1 is ${price1:<20}") 
print(f"Price 2 is ${price2:<20}")
print(f"Price 3 is ${price3:<20}")


# Right justify a value (pushes values to the right with 20 spaces on the left --> like "price1:20")
print(f"Price 1 is ${price1:>20}") 
print(f"Price 2 is ${price2:>20}")
print(f"Price 3 is ${price3:>20}")


# the carrot "^" centers the values 
print(f"Price 1 is ${price1:^20}") 
print(f"Price 2 is ${price2:^20}")
print(f"Price 3 is ${price3:^20}")

#-------------------------------------------------------------------
# the "+" displays any positive number with the + sign 
print(f"Price 1 is ${price1:+}") 
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

# or you could use a space below (note the "$" and the "amount" has a space between them to show positives)

print(f"Price 1 is ${price1: }") 
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")
#---------------------------------------------------------------

# now the "," comma separates the values to make it easier to read (thousands place)
print(f"Price 1 is ${price1:,}") 
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")


# We can also mix and match them
print(f"Price 1 is ${price1:+,.2f}") 
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")

