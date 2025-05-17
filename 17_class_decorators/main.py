# 17. Class Decorators
"""
Assignment:
Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person."""

def add_greeting(cls):
    # New method jo class mein add karni hai
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Class ko naye method se modify karo
    return cls  # Modified class wapas return karo
    
@add_greeting  # Yeh decorator Person class par apply hua
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}."
    
person = Person("Ali")

print(person.introduce())  # Output: My name is Ali.

print(person.greet())      # Output: Hello from Decorator!
    