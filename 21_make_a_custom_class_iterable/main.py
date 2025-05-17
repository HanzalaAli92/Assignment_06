# 21. Make a Custom Class Iterable
"""
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0."""

# Countdown class jo iterable object banata hai
class Countdown:
    def __init__(self, start):
        self.start = start      # Start number set kar raha hai
        self.current = start    # Current value ko start se initialize kar raha hai

    def __iter__(self):
        # Iterator object return kar raha hai (khud ko return kar raha hai)
        return self

    def __next__(self):
        # Agar current number 0 se kam ho gaya, to iteration stop karo
        if self.current < 0:
            raise StopIteration
        # Current number ko ek kam karo
        self.current -= 1
        # Aur previous value return karo
        return self.current + 1

# Countdown object create kar rahe hain start value 5 se
countdown = Countdown(5)

# For loop ke zariye iterable object ko iterate kar rahe hain
for number in countdown:
    print(number)