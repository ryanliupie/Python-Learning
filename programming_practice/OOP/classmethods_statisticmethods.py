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

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'
    
    @classmethod 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_str_1 = "Ryan-Liu-80000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

#------------------------------------------------------------------------------------------

# static methods do not pass "self" or "cls" as its first argument, rather it behaves like regular a function that relates to the class

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: #0123456 --> monday tuesday, wednesday, thursday, friday, saturday, sunday                                               
            return False
        return True
    
import datetime 
my_date = datetime.date(2025, 2, 28)
print(Employee.is_workday(my_date))

# "if the weekday is saturday(5) or sunday(6) return false because this is not a workday. If it is a weekday(0-4) then return true"
# "well today is february 28th 2025 on a friday, so this is true since we are working today"


