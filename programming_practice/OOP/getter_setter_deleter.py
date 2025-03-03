# @property works with getter, setter, and deleter 

class Person:
    def __init__(self, name):
        self.name = name 

    @property # this is the "getter" as it is getting access to the method in order to call it like an attribute
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError
        self._name = value 

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

person = Person("Alice")

print(person.name)

person.name = "Ryan"
print(person.name)