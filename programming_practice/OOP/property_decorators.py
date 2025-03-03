#class Employee:
 #   def __init__(self, first, last):
  #      self.first = first 
   #     self.last = last 
       # self.email = first + "." + last + "@gmail.com"

 #   def full_name(self):
  #      return f"{self.first} {self.last}"


#emp_1 = Employee("Ryan", "Liu")

#print(emp_1.email)
#print(emp_1.full_name())


#----------------------------------------------------------------

# the @property decorator allows me to call the fuction "email" like an attribute with only one bracket

class Employee:
    def __init__(self, first, last):
        self.first = first 
        self.last = last 

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    def full_name(self):
        return f"{self.first} {self.last}"

emp_1 = Employee("Ryan", "Liu")

print(emp_1.email)
