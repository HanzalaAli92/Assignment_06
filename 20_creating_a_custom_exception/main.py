# 20. Creating a Custom Exception
"""
Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except"""

# Custom exception class jo InvalidAgeError ko define karta hai
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)  # Parent Exception class ko initialize karta hai

# Function jo age check karta hai
def check_age(age):
    # Agar age 18 se kam ho to custom exception raise karo
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
    else:
        # Agar age valid ho to ye message print karo
        print(f"Age {age} is valid.")

try:
    # User se input le raha hai aur integer mein convert kar raha hai
    age = int(input("Enter your age: "))
    # Age check karne wali function ko call karo
    check_age(age)

# Agar InvalidAgeError raise hui to is block mein aayega
except InvalidAgeError as e:
    print(e)  # Exception ka message print karega

# Agar input integer nahi hai to ye error handle karega
except ValueError:
    print("Please enter a valid integer for age.")