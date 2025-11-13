class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
    
    def display(self):
        return f"{self.brand} {self.model} - {self.color} - ${self.price}"

# Creating similar objects without prototype
car1 = Car("Toyota", "Camry", "Red", 25000)
car2 = Car("Toyota", "Camry", "Blue", 25000)  # Same brand, model, price - different color
car3 = Car("Toyota", "Camry", "Black", 25000) # Same brand, model, price - different color

print("Without Prototype Pattern:")
print(car1.display())
print(car2.display())
print(car3.display())