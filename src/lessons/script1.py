class Animals():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
if __name__ == "__main__": # "Only run this code if this file "
                           # "is being executed directly, not"
                           # "if its being imported by another file"
    dog1 = Animals("Kylo", 4)
    dog2 = Animals("Koby", 3)

    print(dog1.name, end = ": ")
    print(dog1.age)

    print(dog2.name, end = ": ")
    print(dog2.age)


# so if we run this file, it will be the main, and it will print out both objects 