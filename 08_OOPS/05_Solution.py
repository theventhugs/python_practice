# ***5. Polymorphism***
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fuel_type(self):
        return "Petrol | Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        # return super().fuel_type() # if I had to use to inherited class's value
        return "Battry"

myCar = Car("TATA", "Nexon")
myNewCar = ElectricCar("Tesla", "S9", "80kWh")

print(Car.fuel_type(myCar))
print(ElectricCar.fuel_type(myNewCar))

