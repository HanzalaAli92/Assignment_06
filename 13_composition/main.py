# 13. Composition
"""
Assignment:
Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class."""

class Engine:

    def start(self):
        # Engine start hone ka message print karna
        print("Engine has started")
    
class Car:
    def __init__(self):
        # Composition: Car ke andar Engine object banaya aur store kiya
        self.engine = Engine()

    def start_engine(self):
        # Car ke method se Engine ke start method ko call karna
        self.engine.start()

if __name__ == "__main__":
    car = Car()  # Car ka object banaya
    car.start_engine()  # Car ke zariye Engine start kar rahe hain (Output: Engine has started)