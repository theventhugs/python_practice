# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    @staticmethod
    def general_info(): # No need to use 'self'
        return "Cars are very amazing"

# myCar = Car("TATA", "Nexon") # now we don't need to create any instances to use general info
print(Car.general_info())
