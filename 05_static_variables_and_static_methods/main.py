# 5. Static Variables and Static Methods
"""
Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used."""

# MathUtils naam ka class banaya gaya hai
class MathUtils:
    @staticmethod
    def add(a, b):
        # Static method hai jo sirf do numbers ka sum return karega
        return a + b
    
# Agar yeh file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    # Static method ko class ka object banaye bagair direct call kiya gaya
    result = MathUtils.add(5, 3)
    
    # Result ko print kiya gaya
    print(f"The sum of 5 and 3 is: {result}")