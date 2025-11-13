# Without Bridge Pattern - classes are tightly coupled
class CircleWithRedColor:
    def draw(self):
        return "Drawing Circle with Red color"

class CircleWithBlueColor:
    def draw(self):
        return "Drawing Circle with Blue color"

class SquareWithRedColor:
    def draw(self):
        return "Drawing Square with Red color"

class SquareWithBlueColor:
    def draw(self):
        return "Drawing Square with Blue color"

# Usage
circle_red = CircleWithRedColor()
circle_blue = CircleWithBlueColor()
square_red = SquareWithRedColor()
square_blue = SquareWithBlueColor()

print(circle_red.draw())   # Drawing Circle with Red color
print(square_blue.draw())  # Drawing Square with Blue color