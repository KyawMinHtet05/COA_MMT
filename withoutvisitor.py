class Dog:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says: Woof!"
    
    def feed(self):
        return f"Feeding {self.name} dog food"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} says: Meow!"
    
    def feed(self):
        return f"Feeding {self.name} cat food"

# Usage
animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    print(animal.make_sound())
    print(animal.feed())
    print()  # empty line