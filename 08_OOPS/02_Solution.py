# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_full_name(self): #"Method" is fancy name of "function"
        print(f'Name of the car is: {self.brand} and the model is: {self.model}')



myCar = Car("TATA", "Nexon")

Car.display_full_name(myCar)