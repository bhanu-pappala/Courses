class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print(f'Manufacturer: {self.make}')
        print(f'Color: {self.color}')
        print(f'Model: {self.model}')


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print(f'Doors: {self.doors}')

obj1 = Car("Suzuki", "Blue", "2016", 90)
obj1.printCarDetails()
