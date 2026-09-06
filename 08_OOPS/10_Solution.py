# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def battery_class(self):
        return 'this is from battery class'

class Engine:
    def engine_class(self):
        return 'this is from engine class'

class ElectricCar(Battery, Engine):
    pass

newClass = ElectricCar("TATA", "Nexon")


print(newClass.battery_class())
print(newClass.engine_class())