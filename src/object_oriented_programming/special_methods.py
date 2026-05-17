# Special Methods 
# Simply put "dundar" refers to "double underscores" so any method (__repr__, __str__) that has that is a special method

class Rectangle:
    def __init__(self, width, height): # runs when object is created. Used to initialize attributes (data) for object/instance of a class
        self.width = width 
        self.height = height

    def __repr__(self): # return same as __str__, but intended to be user-friendly for end-users 
        return f" The Rectangle width is {self.width}, and the height is {self.height}"
    
    def __str__(self): # return same as __repr__ but intended for developers (debugging)
        return f"The Rectangle width is {self.width}, and the height is {self.height}"

rect = Rectangle(7,12)

print(repr(rect))
print(str(rect))

