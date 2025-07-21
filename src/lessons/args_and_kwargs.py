# *ARGS = "non-key arguments": Positional arguments are used when you do not know how many arguments passed in a function.
# *args does not have to be that name, it can be something like *num
# you can treat args as a tuple, an immutable collection of items 

def name(*args):
    for arg in args:
        print(f"my name is {arg}\n")

print(name("ryan", "jake", "dylan"))

# **KWARGS = "keyword-arguments": allows you to pass multiple keyword-arguments
# *kwargs does not have to be that name, it can be something like *num
# you can treat kwargs as a dictionary, a key-value pair 

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

print_address(street="Turtle Lane St.", 
              city="Toronto", 
              province="Ontario", 
              postal_code="1T4 QW2")

# --------------------------------------------------

# Combing both args and kwargs 

def shipping_label(*args, **kwargs ): 
    for arg in args:
        print(arg, end=" ")
    print()
    print("----------------------")
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}, {kwargs.get('province')}, {kwargs.get('postal_code')}")
  
    


shipping_label("Professor", "Ryan", "Liu",
                street="Panda Lane St.", 
                city="Toronto", 
                province="Ontario", 
                postal_code="1T4 QW2"
              )