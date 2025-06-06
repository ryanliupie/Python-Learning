menu = {"coffee" : 1.50,
        "icecream" : 1.50, 
        "soda" : 1.50, 
        "poutine" : 5.00, 
        "hotdog" : 3.00, 
        }

cart = []
total = 0 

print("--------MENU--------")
for key, value in menu.items(): 
    print(f"{key:8}: ${value:.2f}")
print("--------------------")

while True: 
    food = input("select a food item (q to quit): ").lower()
    if food == "q": 
        break
    elif menu.get(food) is not None: 
        cart.append(food)
        
for food in cart: 
    total += menu.get(food)
    print(food, end=" ")
print()

print(f"The total is ${total:.2f}")

