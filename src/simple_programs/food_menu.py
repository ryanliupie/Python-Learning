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

choice = input("")