# shopping car program 

foods = []
prices = []
total = 0

while True: 
    food = input("enter a food to buy (q to quit): ")
    if food.lower() == "q": # if user accidently types in upper case "Q", this method turns it into lower so the program would quit
        break
    else:
        price = float(input(f"Enter the price of the {food} (in $): "))
        foods.append(food) # adds person's food to empty list
        prices.append(price) # adds the price to empty list 

separator = ", "
result = separator.join(foods) # when printing, this allows for only "," and not the entire brackets []

for price in prices: 
    total = price + total # adds every inputed price to the total amount starting from 0


print(f"The foods you are buying include --> {result}")
print(f"The total amount is ${total:.1f}")
