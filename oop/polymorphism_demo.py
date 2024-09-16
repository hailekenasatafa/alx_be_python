# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Base method that should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize the Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
