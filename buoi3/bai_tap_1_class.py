import math

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def display(self):
        print(f"Bán kính: {self.radius}")
        print(f"Diện tích: {self.area():.2f}")
        print(f"Chu vi: {self.circumference():.2f}")

radius = float(input("Nhập bán kính hình tròn: "))

circle = Circle(radius)

circle.display()

print("\nThoát chương trình.")
