# 19. callable() and __call__()
"""
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function."""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Factor set karta hai
    
    def __call__(self, num):
        # Jab object ko function ki tarah call karo
        return num * self.factor

# Object create karna factor 5 ke sath
multiplier = Multiplier(5)

# Check karte hain agar object callable hai
print(callable(multiplier))  # Output: True

# Object ko function ki tarah call karte hain
result = multiplier(10)

print(result)  # Output: 50