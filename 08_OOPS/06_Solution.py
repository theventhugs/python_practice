# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_cars = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def fuel_type(self):
        return "Petrol | Diesel"

myCar1 = Car("TATA", "Nexon")
myCar2 = Car("BMW", "M7")
myCar3 = Car("Mahindra", "Thar")

print(Car.total_cars) 
# By this way, we won't need to create a class object just to some small information