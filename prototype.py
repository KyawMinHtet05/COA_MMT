import copy

class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
    
    def clone(self):
        return copy.deepcopy(self)
    
    def display(self):
        return f"{self.brand} {self.model} - {self.color} - ${self.price}"

# Using Prototype pattern
# Create a prototype
prototype_car = Car("Toyota", "Camry", "Red", 25000)

# Clone and customize
car1 = prototype_car.clone()
car1.color = "Blue"

car2 = prototype_car.clone()
car2.color = "Black"

car3 = prototype_car.clone()
car3.color = "White"
car3.price = 27000  # Premium version

print("\nWith Prototype Pattern:")
print(car1.display())
print(car2.display())
print(car3.display())