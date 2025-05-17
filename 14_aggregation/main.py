# 14. Aggregation
"""
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it."""

class Employee:
    def __init__(self, name):
        # Employee ka naam set karna
        self.name = name

class Department:
    def __init__(self, employee):
        # Department ke paas ek Employee object ka reference hai (aggregation)
        self.employee = employee

    def get_employee_name(self):
        # Employee ka naam print karna
        print(f"Employee Name: {self.employee.name}")

if __name__ == "__main__":
    emp = Employee("Ali")  # Employee object banaya

    dept = Department(emp)  # Department object banaya aur employee ka reference pass kiya

    dept.get_employee_name()  # Employee ka naam department ke zariye access kiya