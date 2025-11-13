# With Bridge Pattern - separates abstraction from implementation

# Implementation interface
class Color:
    def apply_color(self):
        pass

# Concrete implementations
class RedColor(Color):
    def apply_color(self):
        return "Red"

class BlueColor(Color):
    def apply_color(self):
        return "Blue"

# Abstraction
class Shape:
    def __init__(self, color):
        self.color = color  # Bridge - composition over inheritance
    
    def draw(self):
        pass

# Refined abstractions
class Circle(Shape):
    def draw(self):
        return f"Drawing Circle with {self.color.apply_color()} color"

class Square(Shape):
    def draw(self):
        return f"Drawing Square with {self.color.apply_color()} color"

# Usage
red = RedColor()
blue = BlueColor()

circle_with_red = Circle(red)
circle_with_blue = Circle(blue)
square_with_red = Square(red)
square_with_blue = Square(blue)

print(circle_with_red.draw())   # Drawing Circle with Red color
print(square_with_blue.draw())  # Drawing Square with Blue color

# Easy to extend - add new color without modifying shapes
class GreenColor(Color):
    def apply_color(self):
        return "Green"

green = GreenColor()
circle_with_green = Circle(green)
print(circle_with_green.draw())  # Drawing Circle with Green color