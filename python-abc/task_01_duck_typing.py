from abc import ABC, abstractmethod
import math

# 1. Define the abstract base class Shape
class Shape(ABC):

    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass

# 2. Concrete class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 3. Concrete class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 4. Duck-typing function
def shape_info(shape):
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 30)

# 5. Testing
circle = Circle(5)
rectangle = Rectangle(4, 6)

shape_info(circle)
shape_info(rectangle)
