class Employee:
     def __init__(self, first, last, email, pay):
        self.first = first
        self.last = last
        self.email = email 
        self.pay = pay

     @staticmethod
     def calculate_annual_salary(hourly_rate, hours_per_week):
        return hourly_rate * hours_per_week * 52

salary = Employee.calculate_annual_salary(45, 40)
print(salary) 


