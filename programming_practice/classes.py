# Python Object-Oriented Programming 

class Employee: 
    pass # this statement tell python to skip it so no error is produced

emp_1 = Employee() #emp_1 is the instance of the class Employee (object) 
emp_2 = Employee() #emp_2 is also the instance of the class Employee (object) 

#print(emp_1, emp_2)

emp_1.first = 'ryan' #attribute 
emp_1.last = 'liu' #attribute 
emp_1.email = 'ryanliu314@gmail.com' #attribute 
emp_1.pay = 5000 #attribute  

emp_2.first = 'bob' #attribute 
emp_2.last = 'dhillon' #attribute 
emp_2.email = 'bob.jake@gmail.com' #attribute 
emp_2.pay = 10000 #attribute  

#print(emp_1.first)
#print(emp_2.first)

#This is no good because everytime a new employee is made, you'd have to manually define the attributes such as first, last, email, and pay for that instance. This is prone to errors and much more difficult to handle as numbers increase. 

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Employee: 
    def __init__(self, first, last, pay): ##def __init__ is what kicks off the creation of objects and prepares them with their specific attribute. Without it, we would have to manually assign every attribute to every object. 
        self.first = first #emp_1.first
        self.last = last  #emp_1.last
        self.pay = pay #emp_1.pay 
        self.email = first + '.' + last + '@gmail.com'

emp_1 = Employee('ryan', 'liu', 5000) #In this case, self just refers to the object right. This means we can reuse the code and make as many objects as we want without having to manually print out each attribute every line. Instead we can do it in one line which reduces a lot of code.
emp_2 = Employee('bob', 'jake', 10000) 

#print(emp_1.email)
#print(emp_2.email)



#--------------------------Now lets add some actions to what our object can do with methods-------------------------------------------------------------------------------------

class Employee: 
    def __init__(self, first, last, pay):  
        self.first = first 
        self.last = last  
        self.pay = pay 
        self.email = first + '.' + last + '@gmail.com'
    
    def fullname(self): #The function or action we want to perform is printing the full name. In the parameter, we need to put self. Remember that self = object. And within that object contains attributes that we need to access in order to perform some type of function and in this case, we are trying to find the full name. So without self, the method/function would not know which objects attributes to use.  
        return f"{self.first} {self.last}" #Remember that 'return' stores the values. In this case, we want to return the first and last name. We F string this because we want to call these attributes when we do decide to print out the full name

emp_1 = Employee('ryan', 'liu', 5000) 
emp_2 = Employee('bob', 'jake', 10000) 

print(emp_1.fullname()) #we need to put another bracket inside just like howe we call a function of fullname
print(emp_2.fullname()) 

## print(Employee.fullname(emp_1)) ----- This is the exact same thing but now we use class and have to manually pass in the instance

