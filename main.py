"""Classmethod-and-staticmethod"""


class Circle:
    """Square circle"""
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """area circle"""
        return self.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """From diameter"""
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius):
        """Check radius"""
        return radius > 0


circle = Circle.from_diameter(10)
area = circle.area()
valid = Circle.check_radius(5)
print(area, valid)
