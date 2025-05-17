# 9. Abstract Classes and Methods
"""
Assignment:
Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area()."""

from abc import ABC, abstractmethod  # abc module se abstract base class aur abstract method ke liye imports

# Abstract base class jo Shape ko represent karti hai
class Shape(ABC):
    
    @abstractmethod  # Yeh method abstract hai, har subclass ko is method ko implement karna zaroori hai
    def area(self):
        pass  # Yahan koi implementation nahi, sirf method signature hai

# Rectangle class jo Shape se inherit karti hai
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width      # Width ko initialize karte hain
        self.height = height    # Height ko initialize karte hain

    def area(self):  # Abstract method area() ko implement kar rahe hain
        return self.width * self.height  # Rectangle ka area nikal rahe hain

if __name__ == "__main__":
    rect = Rectangle(5, 10)  # Rectangle ka object banaya jisme width=5 aur height=10 di gayi
    print(f"Area of the rectangle: {rect.area()}")  # Rectangle ka area print kiya
