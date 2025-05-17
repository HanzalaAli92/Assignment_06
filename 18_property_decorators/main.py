# 18. Property Decorators: @property, @setter, and @deleter
"""
Assignment:
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it."""

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        # Getter method: price ko access karne ke liye
        return self._price

    @price.setter
    def price(self, new_price):
        # Setter method: price update karne ke liye
        if new_price < 0:
            print("Price cannot be negative.")
        else:
            self._price = new_price

    @price.deleter
    def price(self):
        # Deleter method: price delete karne ke liye
        print(f"Deleting the price of {self.name}")
        del self._price

# Usage
product = Product("Phone", 5000)

print(product.price)  # Output: 5000

product.price = 6000
print(product.price)  # Output: 6000

product.price = -400  # Output: Price cannot be negative.

del product.price     # Output: Deleting the price of Phone