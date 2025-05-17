# 3. Public Variables and Methods
"""
Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class."""

# Car naam ka class banaya gaya hai
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable (baar se access kiya ja sakta hai)

    def start(self):  # Public method (baar se call kiya ja sakta hai)
        print(f"{self.brand} is starting.")

# agar yeh file directly run ki jaye to neeche wala code chalega
if __name__ == "__main__":
    my_car = Car("Toyota")  # Car class ka object banaya gaya "Toyota" brand ke saath
    print(my_car.brand)  # Public variable ko class ke baar se access kiya
    my_car.start()  # Public method ko call kiya