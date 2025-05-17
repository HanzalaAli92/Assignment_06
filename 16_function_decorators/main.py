# 16. Function Decorators
"""
Assignment:
Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()."""

def log_function_call(func):
    def wrapper():
        # Jab bhi original function call ho, yeh pehle chalega
        print("Function is being called")
        return func()  # Original function ko call karo
    return wrapper  # Wrapper function return karo

@log_function_call  # Decorator lagaya gaya say_hello function par
def say_hello():
    print("Hello, World!")

if __name__ == "__main__":
    say_hello()  # Jab call karoge, pehle decorator wala message print hoga, phir say_hello ka message