# 8. The super() Function
"""
Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor."""

# Step 1: Parent class banaya gaya hai jiska naam Person hai
class Person:
    def __init__(self, name):
        self.name = name  # name variable initialize kar rahe hain

# Step 2: Child class banayi gayi hai jiska naam Teacher hai
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Parent class ka constructor call kiya super() ki madad se
        self.subject = subject  # subject variable initialize kiya

# Agar file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    teacher = Teacher("Hamza", "Mathematics")  # Teacher ka object banaya
    print(f"Name: {teacher.name}, Subject: {teacher.subject}")  # Dono attributes print kiye

# Step 1: Parent class banaya gaya hai jiska naam Person hai
class Person:
    def __init__(self, name):
        self.name = name  # name variable initialize kar rahe hain

# Step 2: Child class Teacher banayi gayi hai jo Person se inherit karti hai
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Parent class ka constructor call kiya
        self.subject = subject  # subject initialize kiya

    # Step 3: display method banayi gayi hai jo dono values print karegi
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Program ka entry point
if __name__ == "__main__":
    teacher = Teacher("Ali", "Enlish")  # Teacher ka object banaya
    teacher.display()  # Display method call ki
