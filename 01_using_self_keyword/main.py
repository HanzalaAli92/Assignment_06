# 1. Using self

"""Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details."""

# Student naam ka class banaya gaya hai
class Student:
    # Constructor banaya gaya hai jo name aur marks ko initialize karega
    def __init__(self, name, marks):
        self.name = name  # self.name ka matlab hai ke yeh object ka apna name hoga
        self.marks = marks  # self.marks ka matlab hai ke yeh object ke marks hain

    # display function student ki details print karega
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Agar yeh file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    
    # Student class ka ek object banaya jiska name "hamza" aur marks 85 hain
    myClass = Student("hamza", 85)
   
    # display function call karke student ki details print ki gayi
    myClass.display()


