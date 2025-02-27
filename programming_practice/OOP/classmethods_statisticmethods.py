# Class methods are not tied to indivdual objects, but it is tied to the class itself. You use it to change something that applies to all objects of that class.
class Employee:
    num_of_employees = 0 
    raise_amt = 1.13
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_employees += 1 # when another object is created (employee), the number of employees is incremented by 1

    def fullname(self):
        return f"{self.first} {self.last} and he makes {self.pay} a month"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
    
    @classmethod # class method (decorator) to change the class variable of raise_amt. Recieves class of first argument rather the instance "self" where "self" represents the object or instance
    def set_raise_amt(cls, amount): # use "cls" to refer to class itself, not an instance
        cls.raise_amt = amount

emp_1 = Employee('ryan', 'liu', 5000)
emp_2 = Employee('bob', 'james', 3500)

Employee.set_raise_amt(1.15) # changes raise amount from 1.13 to 1.15

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#------------------------------------------------------------------------------------------

# Using class methods as alternative constructors 
# 

class Employee:
    num_of_employees = 0 
    raise_amt = 1.13
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_employees += 1 
    def fullname(self):
        return f"{self.first} {self.last} and he makes {self.pay} a month"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 
    
    @classmethod
    def set_raise_amt(cls, amount): 
        cls.raise_amt = amount

emp_1 = Employee('ryan', 'liu', 5000)
emp_2 = Employee('bob', 'james', 3500)

Employee.set_raise_amt(1.15) 

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
