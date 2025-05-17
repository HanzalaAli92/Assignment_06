# 6. Constructors and Destructors
"""
Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor)."""

# Logger naam ka class banaya gaya hai
class Logger:
    def __init__(self):
        # Constructor: jab object create hota hai to yeh message print hota hai
        print("Logger object created.") 

    def __del__(self):
        # Destructor: jab object destroy hota hai to yeh message print hota hai
        print("Logger object destroyed.")

# Agar yeh file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    
    logger = Logger()  # Logger class ka object banaya gaya

    del logger  # Object ko manually destroy kiya gaya (memory se hata diya)