# Special Methods 
# Simply put "dundar" refers to "double underscores" so any method that has that is a special method

class Rectangle:
    def __init__(self, width, height): # special method
        self.width = width 
        self.height = height

    def __repr__(self): # special method
        return f"Rectangle width = {self.width}, height = {self.height}"
    
    def __str__(self): # special method
        return f"The Rectangle width is {self.width}, and the height is {self.height}"

rect = Rectangle(7,12)

print(repr(rect))
print(str(rect))

