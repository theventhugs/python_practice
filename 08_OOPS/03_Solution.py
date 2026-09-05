# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_full_name(self): #"Method" is fancy name of "function"
        print(f'Name of the car is: {self.brand} and the model is: {self.model}')

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

myCar = Car("TATA", "Nexon")
myNewCar = ElectricCar("Tesla", "S9", "80kWh")

print(myNewCar.brand, myNewCar.model, myNewCar.battery_size)
