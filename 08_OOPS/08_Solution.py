# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model ## to make it private
        Car.total_cars += 1

    @staticmethod
    def general_info(): # No need to use 'self'
        return "Cars are very amazing"

    @property #to make it callable not like a function, but like a property (class.name)
    def model(self):
        return self.__model

myCar = Car("TATA", "Nexon")
# myCar.model = "City" # will throw an error
print(myCar.model)
