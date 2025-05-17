# 12. Static Methods
"""
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value."""

# Task 1
class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Celsius ko Fahrenheit mein convert karne ka formula
        return (c * 9/5) + 32
    
if __name__ == "__main__":
    # 0 Celsius ko Fahrenheit mein convert karke print kar rahe hain
    print("Fahrenheit value of 25 degrees Celsius is: ", TemperatureConverter.celsius_to_fahrenheit(0))


# Task 2
class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Celsius ko Fahrenheit mein convert karne ka formula
        return (c * 9/5) + 32
    
if __name__ == "__main__":
    celsius = 25  # Celsius value set ki
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)  # Conversion static method se ki
    print(f"{celsius}°C is equal to {fahrenheit}°F")  # Result print kar rahe hain