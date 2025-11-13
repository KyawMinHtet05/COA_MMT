class AnimalVisitor:
    def visit_dog(self, dog):
        pass
    
    def visit_cat(self, cat):
        pass

class SoundVisitor(AnimalVisitor):
    def visit_dog(self, dog):
        return f"{dog.name} says: Woof!"
    
    def visit_cat(self, cat):
        return f"{cat.name} says: Meow!"

class Animal:
    def accept(self, visitor):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor):
        return visitor.visit_dog(self)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor):
        return visitor.visit_cat(self)

# Usage
animals = [Dog("Buddy"), Cat("Whiskers")]
sound_visitor = SoundVisitor()

for animal in animals:
    print(animal.accept(sound_visitor))