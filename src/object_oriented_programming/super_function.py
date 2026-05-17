import math

'''
super() lets a child class call methods from its parent class
'''

class Circle: 
    def __init__(self, colour, is_filled, radius): 
        self.colour = colour 
        self.is_filled = is_filled 
        self.radius = radius
    
class Square: 
    def __init__(self, colour, is_filled, width): 
        self.colour = colour 
        self.is_filled = is_filled 
        self.width = width 

class Triangle: 
    def __init__(self, colour, is_filled, width, height): 
        self.colour = colour 
        self.is_filled = is_filled 
        self.width = width 
        self.height = height


# what do these all have in common? Well the attribute colour and is_filled. Lets define these in a main Class
# we can then use the "super()" method to take care all the attributes each of the types of shape have in common also know as the attributes

class Shape: 
    def __init__(self, colour, is_filled): 
        self.colour = colour 
        self.is_filled = is_filled
    
    def describe(self): # extends functionality of inherited methods 
        print(f"The colour is {self.colour} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape): 
    def __init__(self, colour, is_filled, radius): 
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self): # extends functionality of inherited methods 
        area = math.pi * (self.radius ** 2)
        print(f"The area of the circle is {round(area, 2)}")

class Square(Shape): 
    def __init__(self, colour, is_filled, width): 
        super().__init__(colour, is_filled)
        self.width = width 

class Triangle(Shape): 
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width 
        self.height = height

circle = Circle(colour="red", is_filled=True, radius=5)
square = Square(colour="green", is_filled=False, width=6)
triangle = Triangle(colour="blue", is_filled=True, width=8, height=9)

triangle.describe()
circle.describe()