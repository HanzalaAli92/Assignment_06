# 10. Instance Methods
"""
Assignment:
Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name."""

class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable name ko initialize kar rahe hain
        self.breed = breed  # Instance variable breed ko initialize kar rahe hain

    def bark(self):        # Instance method jo dog ka bark message print karega
        print(f"{self.name} says Woof!")  # Dog ka naam aur bark message print kar rahe hain

if __name__ == "__main__":
    my_dog = Dog("Buddy", "Golden Retriever")  # Dog ka object banaya name aur breed ke sath
    my_dog.bark()  # bark method call kiya jo bark message print karega
    print(f"My dog's name is {my_dog.name} and he is a {my_dog.breed}.")  # Dog ke name aur breed ko print kiya
