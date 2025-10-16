list1 = [100, 500, 300, 700, 800, 1, 0, 5]
x = sorted(list1) # use if you want to store new list as a variable 
list1.sort() # use if you dont want to store as variable 

y = sorted(list1, reverse=True) # sorts list in descending order 

print(x)
print(list1)
print(y)

# -------------------------------------------

tuple1 = (500, 6, 7, 1, 67, 32, 34, 56, 3)
s_tup = sorted(tuple1) # must use "sorted() for tuples .sort() only for lists"
print(s_tup)

# -------------------------------------------

dict1 = {"name": "Ryan", "age": 76, "subject": "programming"} 
s_dict = sorted(dict1)
print(s_dict)

# -------------------------------------------

li = [-6, -5, -4, 1, 2 , 3]   
s_li = sorted(li, key=abs, reverse=True) # so instead of -6, it is 6 
print(s_li) 

# -------------------------------------------  

class Employee(): 
    def __init__(self, name, age, salary): 
        self.name = name 
        self.age = age
        self.salary = salary 

    
    def __repr__(self): 
        return f"({self.name}, {self.age}, ${self.salary})"

e1 = Employee("Ryan", 30, 300000) 
e2 = Employee("Jaideep", 30, 300000)
e3 = Employee("Yash",27, 250000)


employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda e: e.name) # lambda creates small anonymous functions
print(s_employees)

