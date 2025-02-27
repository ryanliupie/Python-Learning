class Employee:
    def __init__(self, first, last, email, pay):
        self.first = first 
        self.last = last
        self.email = email 
        self.pay = pay 


    @classmethod
    def from_full_name(cls, full_name, pay):
        first, last = full_name.split(" ")
        email = first.lower() + "." + last.lower() + "@gmail.com"
        return cls(first, last, email, pay)
    
emp1 = Employee.from_full_name("Ryan Liu", "150,000")

print(emp1.first)
print(emp1.last)
print(emp1.email)