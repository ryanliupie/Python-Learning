#lets say that a company gives annual raises a year, where the amount varies every year. One important aspect is that every employee gets the same exact raise. This would be a good class variable because it will be shared across the objects

class Employee:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last} and he makes {self.pay} a month"

    #def apply_raise(self):
        #self.pay = int(self.pay * 1.04) ----this would be inefficent because we would have to manually change the raise in multiple locations, meaning it could be anywhere in the code hiding someplace 


emp_1 = Employee('ryan', 'liu', 5000)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay) ----the issue would be accessing the raise amount specifically, not only the raise added on top


#------------------------------------More efficent way-------------------------------------------------------------------------------------------------------------------

class Employee:
    raise_amt = 1.04 #this is where we will place the class variable instead of putting it in many locations. This way, we can change this portion of the code and it will change everything else along the way
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return f"{self.first} {self.last} and he makes {self.pay} a month"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #to access the class variable, we have to either access the class itself or the instance. But by setting it to self = emp_1, we can change the instance variable if we need to --check line 45 
                                #Employe.raise amount 

emp_1 = Employee('ryan', 'liu', 5000)
emp_2 = Employee('bob', 'james', 3500)

emp_1.raise_amount = 1.05 #this is where we instead using the the class variable, you create a singular variable for a particular employee

print(emp_1.__dict__) #prints out all everything
print(emp_1.raise_amt) #1.05
print(emp_2.raise_amt) #1.04

#print(emp_1.pay) -----5000
#emp_1.apply_raise()---5000  * 1.04   
#print(emp_1.pay)------5200

#print(Employee.raise_amt)----1.04
#print(emp_1.raise_amt)-------1.04 

#-----------------------------------------Lets say we wanted to keep track of the amount of employees we have-------------------------------------------------------------------

class Employee:
    num_of_employees = 0 #class variable 
    raise_amt = 1.13
    
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_employees += 1 #we do not need self because there is no use case for one employee to be different that the total number of employees; from the above example, we used self where we changed the raise value by 1.05 for emp_1; for the total number employees, we can't change 1 employee to = 2; the logic does not make sense

    def fullname(self):
        return f"{self.first} {self.last} and he makes {self.pay} a month"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 

print(Employee.num_of_employees) #initially it will print out 0 

emp_1 = Employee('ryan', 'liu', 5000)
emp_2 = Employee('bob', 'james', 3500)

print(Employee.num_of_employees) #detects 2 employees known as objects or instances of classes and prints out 2

