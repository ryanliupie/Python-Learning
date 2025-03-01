 # Inheritance 

class Employee:
      raise_amt = 1.13

      def __init__(self, first, last, pay):
            self.first = first 
            self.last = last
            self.email = first + "." + last + "@gmail.com" 
            self.pay = pay 

      def full_name(self):
            return self.first + " " + self.last
      
      def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.15

    def __init__(self, first, last, pay, prog_lang): # this allows us to add a new attribute
          super().__init__(first, last, pay) # this allows the "Employee" class to handle first, last, and pay, and allow the "Developer" class to handle prog_lang
          self.prog_lang = prog_lang # same thing 

class Manager(Employee):
      def __init__(self, first, last, pay, employees = None): 
          super().__init__(first, last, pay) 
          if employees is None:
              self.employees = [] # if there are no employees, it will default to an empty list
          else:
              self.employees = employees # allows us to pass attribute when creating an object if there are employees
      
      def add_emp(self, emp): # use self to bind with mgr_1 object 
          if emp not in self.employees: # if employee not in list 
            self.employees.append(emp) # add the employee to the list

      def remove_emp(self, emp):
          if emp in self.employees: # if employee is in the list 
            self.employees.remove(emp) # remove the employee from the list (emp may no longer be under supervision)

      def print_emps(self):
            for emp in self.employees: # for all the employees listed 
                  print("-->", emp.full_name()) # print all the employees with their full name

      
            

dev_1 = Developer("Ryan", "Liu", 50000, "Python")
dev_2 = Developer("Alice", "Khamra", 80000, "Java")

mgr_1 = Manager('Jessica', 'Ace', 93000, [dev_1])

print(mgr_1.email)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager)) # is mgr_1 an instance of Manager? True
print(isinstance(mgr_1, Developer)) # is mgr_1 an instance of Developer? False

print(issubclass(Manager, Employee)) # is Manager a subclass of Employee? True
print(issubclass(Manager, Developer)) # is Manager a subclass of Developer? False




